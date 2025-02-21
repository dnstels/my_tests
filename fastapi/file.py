import io
import os
import shutil
from tempfile import NamedTemporaryFile
import ntpath

from fastapi import UploadFile


def save_temporary(upload_file: UploadFile):
    tmp_dir=os.environ['APP_TMP_DIR']
    with NamedTemporaryFile(
        delete=False, dir=os.path.join(".", tmp_dir), 
        suffix=f"_{upload_file.filename}"
    ) as file_path:
        with open(file_path.name, "wb") as f:
            f.write(upload_file.file.read())
    return file_path.name

def generate_response(filepath: str = None, filename:str=None):
    if filepath:
        filename = filename if filename else ntpath.basename(filepath)
        with open(filepath, "rb") as f:
            contents = f.read()
        # os.remove(filepath)
    else:
        filename = filename if filename else "file.bin"
        with io.BytesIO(b"some initial binary data: \x00\x01") as some_stream:
            contents = some_stream.read()

    headers = {"Content-Disposition": f"attachment; filename={filename}"}
    return headers, contents

def get_path(file_path):
    return os.path.abspath(file_path)

def get_filename(file_path):
    return os.path.basename(file_path)

def get_name_of_file(file_path):
    return os.path.splitext(file_path)

def path_combine(path1, *paths):
    return os.path.join(path1, *paths)

def get_pathfile_temporary(filename):
    tmp_dir=os.environ['APP_TMP_DIR']
    return get_path(path_combine(tmp_dir,filename))

def get_current_dir():
    return os.getcwd()

def change_current_dir(path):
    os.chdir(path)

def make_archive(arc_file_name,dir_for_arc):
    return shutil.make_archive(get_name_of_file(arc_file_name)[0], 'zip', dir_for_arc)
