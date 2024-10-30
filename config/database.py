import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Carga la URL de conexión desde un archivo .env para seguridad
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Configuración de la conexión a MongoDB
class MongoDB:
    def __init__(self, uri: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client["skins-list"]

# Instancia global de MongoDB para usar en toda la aplicación
mongodb = MongoDB(MONGODB_URI)