from config.config import skins_collection
from bson import ObjectId

def convertChampion(champ) -> dict:
    skin_names = [
        skins_collection.find_one({"_id": ObjectId(skin_id)})["skin_name"]
        for skin_id in champ["skins"]
    ]
    
    return {
        "id": str(champ["_id"]),
        "name": champ["name"],
        "skins": skin_names
    }
    
def convertChampions(champs) -> list:
    return [convertChampion(champ) for champ in champs]