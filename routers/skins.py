from fastapi import APIRouter, HTTPException
from app.services.skin_service import SkinService
from app.database import mongodb

skin_router = APIRouter()
skin_service = SkinService(mongodb.db)

@skin_router.get('/skins', tags=['skins'])
async def get_all_skins():
    skins = await skin_service.get_skins()
    return skins