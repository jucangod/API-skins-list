def convertChampion(champ) -> dict:
    return {
        "id": str(champ["_id"]),
        "name": champ["name"],
        "skins": champ["skins[]"]
    }
    
def convertChampions(champs) -> list:
    return [convertChampion(champ) for champ in champs]