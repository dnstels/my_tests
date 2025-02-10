import io
from typing import List

from fastapi import Depends, FastAPI, File, HTTPException, Request, Response, UploadFile
from fastapi.responses import RedirectResponse, StreamingResponse
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tempfile import NamedTemporaryFile

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def save_temporary(upload_file):
    with NamedTemporaryFile(
        delete=False, dir=".\\tmpdir", suffix=f"_{upload_file.filename}"
    ) as file_path:
        with open(file_path.name, "wb") as f:
            f.write(upload_file.file.read())
    return file_path.name

def generate_file_response(filepath=None):
    if filepath:
        with open(filepath, "rb") as f:
            contents = f.read()  # file contents could be already fully loaded into RAM
    else:
        with io.BytesIO(b"some initial binary data: \x00\x01") as some_stream:
            contents=some_stream.read()
    headers = {
        "Content-Disposition": "attachment; filename=file.bin"
    }
    return headers,contents
    

@app.get("/",include_in_schema=False)
def get_root():
    return RedirectResponse(url='/docs')

@app.get("/first")
async def first():
    return {"Hello": "World"}

@app.get("/err500")
async def server_error_handler():
    exc="Текст ошибки"
    raise HTTPException(status_code=500,detail=exc)

@app.get("/ping")
async def ping():
    return "ok"

@app.get('/get_file_as_stream')
def getfile_as_stream():
    headers,some_data=generate_file_response()
    return Response(content=some_data, media_type="application/octet-stream", headers=headers)

@app.post("/convert")
# async def convert(myfile: UploadFile):
async def convert(files: List[UploadFile] = File(...)):
    f1=files[0]
    print(f1.filename)
    myfile=f1
    file=save_temporary(myfile)
    headers,content=generate_file_response(filepath=file)
    # return file
    # return Response(content=myfile.file, media_type=myfile.content_type, headers=myfile.headers)
    return Response(content=content, media_type="application/octet-stream", headers=headers)
    # return "Ok"


@app.post("/convert_2")
def read_item_via_request_body(request: Request):
    
    print(request)
    form_data = request.form()
    
    # ... Data management operations here ...
    
    return form_data

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)