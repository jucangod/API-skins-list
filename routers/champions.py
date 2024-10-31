from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.config import champions_collection

champions_router = APIRouter()

@champions_router.get('/champions')
async def get_champions():
    champions = champions_collection.find()
    return champions