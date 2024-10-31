from fastapi import APIRouter
from services.champions import ChampionService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

champions = APIRouter()

# Obtener todos los campeones
@champions.get('/champions', tags=['champion'])
async def get_champions():
    service = ChampionService()
    champions = await service.get_champions()
    return JSONResponse(content=jsonable_encoder(champions))
