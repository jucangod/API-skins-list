from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jcespinozarodriguez:3sP0RtduIj7JM03G@skins-wish-list.dteyc.mongodb.net/?retryWrites=true&w=majority&appName=skins-wish-list"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.skins_list
champions_collection = db['champions']
skins_collection = db['skins']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)