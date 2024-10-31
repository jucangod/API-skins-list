def convertSkin(skin) -> dict:
    return {
        "id": str(skin["_id"]),
        "skin_name": skin["skin_name"],
        "release_date": skin["release_date"],
        "isOwned": skin["isOwned"],
        "isWished": skin["isWished"],
        "url": skin["url"]
    }
    
def convertSkins(skins) -> list:
    return [convertSkin(skin) for skin in skins]