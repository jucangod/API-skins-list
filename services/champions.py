from config.database import champions_collection as colection

class ChampionService():
    async def get_champions(self):
        champions_docs = colection.find()
        champions = await champions_docs.to_list()
        return champions