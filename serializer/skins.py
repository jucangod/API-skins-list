from bson import ObjectId
from config.config import champions_collection

def convertSkin(skin) -> dict:
    champion_id = skin["champion_id"]
    champion_name = champions_collection.find_one({"_id": ObjectId(champion_id)})["name"]
    
    return {
        "id": str(skin["_id"]),
        "skin_name": skin["skin_name"],
        "release_date": skin["release_date"],
        "isOwned": skin["isOwned"],
        "isWished": skin["isWished"],
        "url": skin["url"],
        "champion": champion_name
    }
    
def convertSkins(skins) -> list:
    return [convertSkin(skin) for skin in skins]