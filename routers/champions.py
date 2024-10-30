from fastapi import APIRouter, HTTPException
from app.services.champion_service import ChampionService
from app.database import mongodb
from bson import ObjectId

champion_router = APIRouter()
champion_service = ChampionService(mongodb.db)

@champion_router.get('/champions', tags=['champions'])
async def get_champions():
    champions = await champion_service.get_champions()
    return champions