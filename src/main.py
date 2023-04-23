from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient
import multiprocessing
import uvicorn

from src.api.server import init_api
from src.infastructure.database.mongo import get_client

app: FastAPI = init_api()

@app.on_event("startup")
async def startup_event():
    app.client: AsyncIOMotorClient = await get_client()
    app.db: AsyncIOMotorDatabase = app.client['user-auth']
    
@app.on_event("shutdown")
def shutdown_event():
    app.client.close()

if __name__=="__main__":
    uvicorn.run(
        "main:app", 
        host="localhost", 
        port=2000, 
        workers=multiprocessing.cpu_count()*2+1
    )