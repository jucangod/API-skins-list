from fastapi import FastAPI
from routers.champions import champions
from routers.skins import skins

app = FastAPI()
app.title = 'FastAPI Skins List'
app.version = '0.0.1'

app.include_router(champions)
app.include_router(skins)

@app.get('/')
def message():
    return "Hello world!"