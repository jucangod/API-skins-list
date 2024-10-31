from fastapi import FastAPI
from routers.champions import champions_router

app = FastAPI()
app.include_router(champions_router)