from fastapi import FastAPI
# from app.routers.champion_router import champion_router
# from app.routers.skin_router import skin_router

app = FastAPI()
# app.title = 'FastAPI Skins List'
# app.version = '0.0.1'

# app.include_router(champion_router)
# app.include_router(skin_router)

# Base.metadata.create_all(bind=engine)

@app.get('/')
def message():
    return "Hello world!"