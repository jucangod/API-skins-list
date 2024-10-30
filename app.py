from fastapi import FastAPI
from routers.champions import champions
from routers.skins import skins

app = FastAPI()

app.include_router(champions)
app.include_router(skins)