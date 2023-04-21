from fastapi import FastAPI
import multiprocessing
import uvicorn

from src.api.server import init_api

app: FastAPI = init_api()

if __name__=="__main__":
    uvicorn.run(
        "main:app", 
        host="localhost", 
        port=2000, 
        workers=multiprocessing.cpu_count()*2+1
    )