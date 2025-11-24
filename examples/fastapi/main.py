
import os
import io
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import sys

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, JSONResponse

from typing_extensions import Annotated

sys.path.append(".")
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, APIRouter, HTTPException, Query, Response, File, UploadFile
from fastapi.responses import RedirectResponse, HTMLResponse, StreamingResponse

from fastapi import (
    Cookie,
    # FastAPI,
    WebSocket,
    WebSocketException,
    WebSocketDisconnect,
    status,
)

import uvicorn
# from routes import router as router_api

# import helpers.russian_argparse as argparse
from starlette.exceptions import HTTPException as StarletteHTTPException
from uvicorn.config import LOGGING_CONFIG
from pydantic import BaseModel

import time

from rst2html import rst2html
import markdown

from openai import OpenAI

class Item(BaseModel):
    message: str

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        await websocket.close()

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

def messages(data):
    return [
            {"role": "system", "content": "Ты технический писатель. Пиши только на русском языке. Описывай только суть."},
            {"role": "user", "content": f"""Пожалуйста, напишите 
                не вдаваясь в подробности отформатированное markdown сообщение 
                на русском языке для git commit,
                используя результат команды git diff:
                ```
                {data}
                ```
                используй шаблон вывода:

                ```
                {{Краткий заголовок}}

                {{Описание изменений}}
                ```
                
                """}

            ]

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("*****Start*******")
    # tmpdir=os.environ['APP_TMP_DIR']
    tmpdir='.'
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    yield
    print("******Shutdown*******")

def create_app():
    app = FastAPI(lifespan=lifespan)
    # app.include_router(router_api)
    app.mount("/static", StaticFiles(directory="AI/static"), name="static")
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    templates = Jinja2Templates(directory="AI/templates")
    
    @app.exception_handler(RequestValidationError)
    def validation_exception_handler(request: Request, exc: RequestValidationError):
        print(exc)
        err="Ошибка в запросе. Не указан GUID документа."
        return templates.TemplateResponse(
            "error.html",context={'request': request,'error':err}, status_code=422)
    
    @app.exception_handler(404)
    def pagenotfound_exception_handler(request: Request, exc: Exception):
        print(exc)
        err="Запрошена несуществующая страница."
        return templates.TemplateResponse(
            "error.html",context={'request': request,'error':err}, status_code=404)
    
    @app.exception_handler(StarletteHTTPException)
    
    @app.exception_handler(500)
    async def custom_http_exception_handler(request, exc):
        print(exc)
        err="Внутренняя ошибка сервера отображения спецификаций (SpecView). Обратитесь в техподдержку."
        return templates.TemplateResponse(
            "error.html",context={'request': request,'error':err}, status_code=500)
    
    @app.get('/favicon.ico', include_in_schema=False)
    async def favicon():
        return FileResponse('AI/static/favicon.ico')

    @app.get("/", include_in_schema=False)
    async def root():
        # return RedirectResponse("docs")
        # return RedirectResponse("/test/chat")
        return RedirectResponse("/test/chat_stream")
    
    @app.get("/test/chat", response_class=HTMLResponse)
    async def get_test_chat(request: Request):
        return templates.TemplateResponse("chat_index.html", context={
            'request': request,
            'content':'content'
        })
    
    @app.get("/test/chat_stream", response_class=HTMLResponse)
    async def get_test_chat(request: Request):
        return templates.TemplateResponse("chat_ws_test.html", context={
            'request': request,
            'content':'content'
        })

    @app.post('/chat')
    def chat_handler(item: Item):
        user_message = item.message
        return JSONResponse({"reply": user_message})
    
    def generate_response(data):
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
        completion = client.chat.completions.create(
            model="local-model", # this field is currently unused
            messages=messages(data),
            temperature = 0.8,
            # max_tokens = 100,
            stream = False
            )

        return completion.choices[0].message.content
    
    def generate_response_as_stream(data):
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
        completion = client.chat.completions.create(
            model="local-model", # this field is currently unused
            messages=messages(data),
            temperature = 0.5,
            # max_tokens = 100,
            stream = True
            )
        
        # if(stream):
        # # Process streaming response
        for chunk in completion:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")
                yield chunk.choices[0].delta.content
        # else:
        # return completion.choices[0].message.content
                
    @app.post("/uploadfile/")
    async def create_upload_files(
        file: Annotated[
            UploadFile, File(description="File as UploadFile")
        ],
    ):
        # print(file.filename)
        data = file.file.read()
        
        data_out = generate_response(data)
        html = markdown.markdown(data_out.replace('```markdown','').replace('```',''))
        html1, warning = rst2html(data_out)
        return {
            "filename": file.filename,
            "data":  html
            }
    
    import time
    @app.websocket("/ws/{client_id}")
    async def websocket_endpoint(websocket: WebSocket, client_id: int):
        await manager.connect(websocket)
        try:
            # while True:
                data = await websocket.receive_text()
                # print(data)
                
                # await manager.send_personal_message(f"You wrote: {data}", websocket)
                # await manager.broadcast(f"Client #{client_id} says: {data}")
                # await manager.send_personal_message("qwer", websocket)

                # for i in data:
                #     time.sleep(0.1)
                #     await manager.send_personal_message(i, websocket)

                client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
                completion = client.chat.completions.create(
                    model="local-model", # this field is currently unused
                    messages=messages(data),
                    temperature = 1.0,
                    # max_tokens = 100,
                    stream = True
                    )
                
                # if(stream):
                # # Process streaming response
                output = io.StringIO()
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        print(chunk.choices[0].delta.content, end="")
                        print(chunk.choices[0].delta.content, file=output, end="")
                        contents = output.getvalue().replace('```markdown','').replace('```','')
                        await manager.send_personal_message(markdown.markdown(contents), websocket)
                        # await manager.send_personal_message(markdown.markdown(chunk.choices[0].delta.content), websocket)
                        # yield chunk.choices[0].delta.content

                output.close()
                await manager.disconnect(websocket)
        except WebSocketDisconnect:
            await manager.disconnect(websocket)
            await manager.broadcast(f"Client #{client_id} left the chat")
    
    async def fake_video_streamer():
        for i in range(10):
            yield "some fake video bytes"

    return app

app = create_app()
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
