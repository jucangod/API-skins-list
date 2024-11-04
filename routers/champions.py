from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.config import champions_collection
from serializer.champions import convertChampion, convertChampions

champions = APIRouter()

@champions.get('/champions')
def get_champions():
    champions = champions_collection.find()
    converted_data = convertChampions(champions)
    return JSONResponse(content=jsonable_encoder(converted_data))