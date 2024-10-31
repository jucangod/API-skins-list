from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.config import skins_collection
from serializer.skins import convertSkin, convertSkins

skins = APIRouter()

@skins.get('/skins')
def get_skins():
    skins = skins_collection.find()
    convertedSkins = convertSkins(skins)
    return JSONResponse(content=jsonable_encoder(convertedSkins))