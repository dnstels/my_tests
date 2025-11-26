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
import aiohttp
import json 
import openai_async
from openai import AsyncOpenAI


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

def messages_1(data):
    return [
            # {"role": "system", "content": "Ты технический писатель. Пиши только на русском языке. Описывай только суть."},
            {"role": "user", "content": f"""Ты технический писатель. Пиши только на русском языке. Описывай только суть.
Напиши не вдаваясь в подробности отформатированное markdown сообщение на русском языке для git commit, нужно только описание изменения кода используя результат команды git diff, 
'-' в начале сроки означает что строка удалена '+' что строка добавлена, определи изменения:
```
{data}
```
используй шаблон вывода:
```
{{Краткий заголовок, что сделано}}

{{Описание изменений}}
```

"""}

            ]
def messages_2(data):
    return [
            {"role": "system", "content": "You're a technical writer. Write only in Russian. Describe only the essence."},
            # {"role": "user", "content": "Напиши не вдаваясь в подробности и без информации о том что ты понял отформатированное сообщение на русском языке для git commit, нужно только описание изменения кода используя результат команды git diff, определи изменения"},
            {"role": "system", "content": "Прочитай результат команды git diff, определи изменения"},
            {"role": "system", "content":"""Пиши по‑русски, просто и по делу. 
             Соблюдай структуру: заголовок (до 80 знаков), текст (3–5 коротких абзацев), итог (1 строка). 
             Держи нейтрально‑деловой тон и фактуру. Выдай только указанные блоки в указанном порядке.
             """},
            {"role": "user", "content": f"{data}"},
            ]

def messages(data):
    return [
            {"role": "system", "content": "You're a technical writer. Write only in Russian. Describe only the essence."},
            {"role": "user", "content": f"{data}"},
            {"role": "user", "content": "Напиши не вдаваясь в подробности отформатированное сообщение на русском языке для git commit, нужно только описание изменения кода используя результат команды git diff, определи изменения"},
            {"role": "user", "content":"Выведи ответ в виде двух блоков: Краткий заголовок, что сделано, Описание изменений"}
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
    
    async def generate_response(data):
        client = AsyncOpenAI(
            base_url="http://srt-w000007.samba.gazpromproject.ru:8888/v1", 
            api_key="not-needed",
            timeout= 90
            # timeout=2,
            # payload={
            #     "model": "local-model",
            #     "messages": [{"role": "user", "content": "Hello!"}],
            # },
        )
        try:
            response  = await client.chat.completions.create(
                model="local-model", # this field is currently unused
                messages=messages_2(data),
                temperature = 0.5,
                # max_tokens = 100,
                stream = False
                )
            print(response.choices[0].message.content)
            return response.choices[0].message.content
        except :
            print("Request timed out.")
            return "Request timed out."

    async def generate_response_2(data):
        # client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
        # client = OpenAI(base_url="http://srt-w000007.samba.gazpromproject.ru:8888/v1", api_key="not-needed")
        # completion = client.chat.completions.create(
        #     model="local-model", # this field is currently unused
        #     messages=messages_2(data),
        #     temperature = 0.5,
        #     # max_tokens = 100,
        #     stream = False
        #     )

        # return completion.choices[0].message.content
         # URL сервера
            server_url = "http://srt-w000007.samba.gazpromproject.ru:8888/completion"

            # Данные для запроса
            payload = {
                "prompt": f"""Ты технический писатель. Пиши только на русском языке. Описывай только суть.
Напиши не вдаваясь в подробности отформатированное markdown сообщение на русском языке для git commit, нужно только описание изменения кода используя результат команды git diff, 
'-' в начале сроки означает что строка удалена '+' что строка добавлена, определи изменения:
```
{data}
```
используй шаблон вывода:
```
{{Краткий заголовок, что сделано}}

{{Описание изменений}}
```

""",  # Ваш промпт
                # "n_predict": 200,  # Максимальное количество токенов для генерации
                "temperature": 0.5,  # Параметр случайности (0.1-1.0)
                # "stop": ["\n", "###"]  # Строки, при которых генерация останавливается
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(server_url, json=payload) as response:
            # Запрос на сервер  
            # response = requests.post(server_url, json=payload)
                    result_txt = await response.text()
                    print(result_txt)
            # Парсим ответ
            # result = response.json()
            result = json.loads(result_txt)
            completion = result['content']
            return completion
    
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
        
        data_out = await generate_response(data)
        html = markdown.markdown(data_out.replace('```markdown','').replace('```',''))
        html1, warning = rst2html(data_out)
        return {
            "filename": file.filename,
            "data":  html
            }
    
    @app.post("/uploadfile_ci/")
    async def create_upload_files(
        file: Annotated[
            UploadFile, File(description="File as UploadFile")
        ],
    ):
        # print(file.filename)
        data = file.file.read()
        
        data_out = await generate_response(data)
        return data_out.replace('```markdown','').replace('```','')
    
    import time
    import requests
    @app.websocket("/ws/{client_id}")
    async def websocket_endpoint(websocket: WebSocket, client_id: int):
        await manager.connect(websocket)
        try:
            data = await websocket.receive_text()
            # # client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
            # client = OpenAI(base_url="http://srt-w000007.samba.gazpromproject.ru:8888/v1", api_key="not-needed")
            # completion = client.chat.completions.create(
            #     model="local-model", # this field is currently unused
            #     messages=messages_2(data),
            #     temperature = 0.5,
            #     # max_tokens = 100,
            #     stream = True
            #     )
            # URL сервера
            server_url = "http://srt-w000007.samba.gazpromproject.ru:8888/completion"

            # Данные для запроса
            payload = {
                "prompt": "Я люблю есть",  # Ваш промпт
                "n_predict": 200,  # Максимальное количество токенов для генерации
                "temperature": 0.2,  # Параметр случайности (0.1-1.0)
                "stop": ["\n", "###"]  # Строки, при которых генерация останавливается
            }

            # Запрос на сервер  
            response = requests.post(server_url, json=payload)

            # Парсим ответ
            result = response.json()
            completion = result['content']
            
            output = io.StringIO()
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="")
                    print(chunk.choices[0].delta.content, file=output, end="")
                    contents = output.getvalue().replace('```markdown','').replace('```','')
                    await manager.send_personal_message(markdown.markdown(contents), websocket)

            output.close()
            await manager.disconnect(websocket)
        except WebSocketDisconnect:
            await manager.disconnect(websocket)
    
    async def fake_video_streamer():
        for i in range(10):
            time.sleep(0.5)
            yield "some fake video bytes"

    return app

app = create_app()
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
