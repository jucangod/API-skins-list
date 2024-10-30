from config.database import skins_collection

class SkinsService():
    async def get_skins(self):
        skins_docs = skins_collection.find()
        skins = await skins_docs.to_list()
        return skins
    
    async def get_missing_skins(self):
        skins_docs = skins_collection.find({
            "$and": [
                {"isOwned": False},
                {"isWished": False}
            ]
        })
        skins = await skins_docs.to_list()
        return skins
    
    async def get_missing_skins(self):
        skins_docs = skins_collection.find({
            "$and": [
                {"isOwned": False},
                {"isWished": False}
            ]
        })
        skins = await skins_docs.to_list()
        return skins
    
    async def get_wished_skins(self):
        skins_docs = skins_collection.find({
            "$and": [
                {"isOwned": False},
                {"isWished": True}
            ]
        })
        skins = await skins_docs.to_list()
        return skins
    
    async def get_owned_skins(self):
        skins_docs = skins_collection.find({
            "$and": [
                {"isOwned": True},
                {"isWished": False}
            ]
        })
        skins = await skins_docs.to_list()
        return skins