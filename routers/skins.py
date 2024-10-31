# from fastapi import APIRouter
# from services.skins import SkinsService
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder

# skins = APIRouter()

# #Obtener todas las skins
# @skins.get('/skins', tags=['skins'])
# async def get_skins():
#     service = SkinsService()
#     skins = await service.get_skins()
#     return JSONResponse(content=jsonable_encoder(skins))

# #Obtener skins obtenidas
# @skins.get('/skins/owned', tags=['skins'])
# async def get_owned_skins():
#     service = SkinsService()
#     skins = await service.get_owned_skins()
#     return JSONResponse(content=jsonable_encoder(skins))

# #Obtener skins deseadas
# @skins.get('/skins/wished', tags=['skins'])
# async def get_wished_skins():
#     service = SkinsService()
#     skins = await service.get_wished_skins()
#     return JSONResponse(content=jsonable_encoder(skins))

# #Obtener skins faltantes
# @skins.get('/skins/missing', tags=['skins'])
# async def get_missing_skins():
#     service = SkinsService()
#     skins = await service.get_missing_skins()
#     return JSONResponse(content=jsonable_encoder(skins))