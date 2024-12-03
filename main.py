import uuid
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.test_database  
collection = db.test_collection 

def create_random_document():

    document = {
        "UUID": str(uuid.uuid4()),
        "name": "RandomName",
        "value": 100  # Arbitrary fields for demonstration
    }
    collection.insert_one(document)
    return document["UUID"]
