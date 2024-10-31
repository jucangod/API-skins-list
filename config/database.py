import os
import motor.motor_asyncio
from fastapi import FastAPI

app = FastAPI()

MONGODB_URL="mongodb+srv://jcespinozarodriguez:3sP0RtduIj7JM03G@skins-wish-list.dteyc.mongodb.net/?retryWrites=true&w=majority&appName=skins-wish-list"

# Create a new client and connect to the server 
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

db = client.get_database("skins_list")
champions_collection = db.get_collection("champions")
skins_collection = db.get_collection("skins")

# Send a ping to confirm a successful connection 
try:     
    client.admin.command('ping')     
    print("Pinged your deployment. You have successfully connected to MongoDB!") 
except Exception as e:     
    print(e) 
