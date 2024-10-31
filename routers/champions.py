from fastapi import APIRouter
from config.config import champions_collection
champions_router = APIRouter()

@champions_router.get('/champions')
def get_champions():
    champions = champions_collection.find()
    return champions