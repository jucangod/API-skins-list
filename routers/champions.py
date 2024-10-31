from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.config import champions_collection
from serializer.champions import convertChampion, convertChampions

champions = APIRouter()

@champions.get('/champions')
def get_champions():
    champions = champions_collection.find()
    convertedChampions = convertChampions(champions)
    return JSONResponse(content=jsonable_encoder(convertedChampions))