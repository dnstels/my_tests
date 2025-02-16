import asyncio
from http import HTTPStatus
from fastapi import BackgroundTasks
from typing import Dict, List
from uuid import UUID, uuid4
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware



class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    status: str = "in_progress"
    progress: int = 0
    result: int = None


app = FastAPI()
jobs: Dict[UUID, Job] = {}  # Dict as job storage

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def long_task(queue: asyncio.Queue, param: int):
    for i in range(1, param):  # do work and return our progress
        await asyncio.sleep(1)
        await queue.put(i)
    await queue.put(None)


async def start_new_task(uid: UUID, param: int) -> None:

    queue = asyncio.Queue()
    task = asyncio.create_task(long_task(queue, param))

    while progress := await queue.get():  # monitor task progress
        jobs[uid].progress = progress

    jobs[uid].status = "complete"


@app.post("/new_task/{param}", status_code=HTTPStatus.ACCEPTED)
async def task_handler(background_tasks: BackgroundTasks, param: int):
    new_task = Job()
    jobs[new_task.uid] = new_task
    background_tasks.add_task(start_new_task, new_task.uid, param)
    return new_task


@app.get("/task/{uid}/status")
async def status_handler(uid: UUID):
    return jobs[uid]

@app.get("/ping")
async def ping():
    new_task = Job()
    return new_task

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("main_2:app", host="localhost", port=8000, reload=True)