import asyncio
import os
import tempfile

from helpers.file import change_current_dir, get_current_dir, make_archive, path_combine


async def long_task(queue: asyncio.Queue, param: int):
    for i in range(1, param):  # do work and return our progress
        await asyncio.sleep(1)
        await queue.put(i)
    await queue.put(None)


async def split_sheets(queue: asyncio.Queue, file_name: str, sheets):
    tmp_dir=os.environ['APP_TMP_DIR']
    with tempfile.TemporaryDirectory(dir=path_combine(get_current_dir(),tmp_dir)) as tmp_subdir:
        change_current_dir(path_combine(tmp_dir,tmp_subdir))
        os.replace(file_name,f"{path_combine(get_current_dir(),'infile.xlsx')}")

        command=os.environ['CMD_DOCCONSTRUCTOR']
        # arg2='../../app/docbuilder_files/split_sheet.docbuilder'
        arg2='/app/docbuilder_files/split_sheet.docbuilder'
        task_index=0
        for item in sheets:
            task_index+=1
            # arg1=f'"--argument={{\\"NameSheet\\":\\"{item}\\"}}"'
            task=asyncio.create_task(call_command(command, item, arg2))
            await task
            await queue.put((task_index,item))
        os.remove("infile.xlsx")
        change_current_dir("../")
        out_file_path=make_archive(file_name, tmp_subdir)
    change_current_dir("../")
    await queue.put(None)
    return out_file_path

async def call_command(command,item,arg2):
    arg1=f'"--argument={{\\"NameSheet\\":\\"{item}\\"}}"'
    # print(f'{command} {arg1} {arg2}')
    # os.system(f'{command} {arg1} {arg2}')
    proc = await  asyncio.create_subprocess_shell(f'{command} {arg1} {arg2}')
    await proc.communicate()

    if os.path.exists('outFile.xlsx'):
        os.rename('outFile.xlsx', f'{item}.xlsx')
    if os.path.exists('outFile.pdf'):
        os.rename('outFile.pdf', f'{item}.pdf')
