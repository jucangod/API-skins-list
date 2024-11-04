from bson import ObjectId
from config.config import champions_collection

def convertSkin(skin) -> dict:
    # Obtener el nombre del campeón utilizando `champion_id` en la colección de campeones
    champion = champions_collection.find_one({"_id": skin["champion_id"]})
    
    return {
        "id": str(skin["_id"]),
        "skin_name": skin["skin_name"],
        "release_date": skin["release_date"],
        "isOwned": skin["isOwned"],
        "isWished": skin["isWished"],
        "url": skin["url"],
        "champion": champion["name"] if champion else None  # Asegurarse de manejar casos donde el campeón no existe
    }
    
def convertSkins(skins) -> list:
    return [convertSkin(skin) for skin in skins]