from config.database import champions_collection as colection

print(colection)

class ChampionService():
    async def get_champions(self):
        champions_docs = colection.find()
        champions = await champions_docs.to_list()
        print("Campeones recibidos ", champions)
        return champions
