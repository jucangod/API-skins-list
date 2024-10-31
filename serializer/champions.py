def convertChampion(champ) -> dict:
    return {
        "id": str(champ["_id"]),
        "name": champ["name"],
        "skins": [str(skin_id) for skin_id in champ["skins"]]
    }
    
def convertChampions(champs) -> list:
    return [convertChampion(champ) for champ in champs]