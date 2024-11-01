from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.config import skins_collection
from serializer.skins import convertSkin, convertSkins

skins = APIRouter()

#Obtener todas las skins en general
@skins.get('/skins')
def get_skins():
    skins = skins_collection.find()
    convertedSkins = convertSkins(skins)
    return JSONResponse(content=jsonable_encoder(convertedSkins))

#Obtener skins faltantes
@skins.get('/skins/missing')
def get_missing_skins():
    conditions = [
        {"isWished": False},
        {"isOwned": False}
    ]
    
    skins = skins_collection.find({
        "$and": conditions
    })
    convertedSkins = convertSkins(skins)
    return JSONResponse(content=jsonable_encoder(convertedSkins))

#Obtener skins deseadas
@skins.get('/skins/wished')
def get_wished_skins():
    conditions = [
        {"isWished": True},
        {"isOwned": False}
    ]
    
    skins = skins_collection.find({
        "$and": conditions
    })
    convertedSkins = convertSkins(skins)
    return JSONResponse(content=jsonable_encoder(convertedSkins))

#Obtener skins obtenidas
@skins.get('/skins/owned')
def get_owned_skins():
    conditions = [
        {"isWished": False},
        {"isOwned": True}
    ]
    
    skins = skins_collection.find({
        "$and": conditions
    })
    convertedSkins = convertSkins(skins)
    return JSONResponse(content=jsonable_encoder(convertedSkins))

#Añadir una skin deseada
@skins.put('/skins/wished')
def add_wished_skins(skin_id: str):
    query = {"_id": ObjectId(skin_id)}
    update = {"$set": {"isWished": True}}
    skins_collection.update_one(query, update)
    updated_skin = skins_collection.find_one(query)
    convertedSkins = convertSkins(updated_skin)
    return JSONResponse(content=jsonable_encoder(convertedSkins))

#Añadir una skin obtenida
@skins.put('/skins/owned')
def add_owned_skins(skin_id: str):
    query = {"_id": ObjectId(skin_id)}
    update = {"$set": {"isOwned": True}}
    skins_collection.update_one(query, update)
    updated_skin = skins_collection.find_one(query)
    convertedSkins = convertSkins(updated_skin)
    return JSONResponse(content=jsonable_encoder(convertedSkins))

#Eliminar skin
@skins.put('/skins')
def delete_skins(skin_id: str):
    query = {"_id": ObjectId(skin_id)}
    update = {
        "$set": {
            "isOwned": False,
            "isWished": False
        }
    }
    skins_collection.update_one(query, update)
    updated_skin = skins_collection.find_one(query)
    convertedSkins = convertSkins(updated_skin)
    return JSONResponse(content=jsonable_encoder(convertedSkins))