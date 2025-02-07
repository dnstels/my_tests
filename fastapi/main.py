import io
import time
from urllib.request import Request
from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.responses import RedirectResponse, StreamingResponse
# from sqlalchemy.orm import Session
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",include_in_schema=False)
def get_root():
    return RedirectResponse(url='/docs')

@app.get("/first")
async def first():
    return {"Hello": "World"}

# @app.exception_handler(Exception)
@app.get("/err500")
# async def server_error_handler(request: Request, exc: Exception):
async def server_error_handler():
    exc="Текст ошибки"
    # time.sleep(5)
    # return JSONResponse(
    #     status_code=500,
    #     content={"detail": str(exc)},
    # )
    raise HTTPException(status_code=500,detail=exc)

@app.get("/ping")
async def ping():
    return "ok"

@app.get('/get_file_as_stream')
def getfile_as_stream():
    # with open(filepath, "rb") as f:
    #     contents = f.read()  # file contents could be already fully loaded into RAM

    # some_stream= io.BytesIO(b"some initial binary data: \x00\x01")
    with io.BytesIO(b"some initial binary data: \x00\x01") as some_stream:
        some_data=some_stream.read()

    # headers = {'Content-Disposition': f'attachment; filename="{filename}"'}
    # return Response(contents, headers=headers, media_type='audio/mp3')

    headers = {
        "Content-Disposition": "attachment; filename=file.bin"
    }

    # return StreamingResponse(some_stream, media_type="application/octet-stream")
    return Response(content=some_data, media_type="application/octet-stream", headers=headers)

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
