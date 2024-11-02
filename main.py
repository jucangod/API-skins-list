from fastapi import FastAPI
from routers.champions import champions
from routers.skins import skins
from middleware.cors import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

app.include_router(champions)
app.include_router(skins)