from fastapi import APIRouter

class ChampionService():
    
    def __init__(self, db) -> None:
        self.db = db
    
    def get_champions(self):
        result = self.db.query(ChampionModel).all()