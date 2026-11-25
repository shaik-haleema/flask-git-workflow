import os
import certifi
from pymongo import MongoClient

mongo_uri = os.environ.get("MONGODB_URI")

client = MongoClient(
    mongo_uri,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

db = client["todo_database"]

collection = db["todo_items"]