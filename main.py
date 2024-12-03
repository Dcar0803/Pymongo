import uuid
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.test_database  
collection = db.test_collection 

def create_random_document():

    """
    Create a random MongoDB document with a UUID field and return the UUID.

    Returns:
        str: UUID of the created document
    """

    document = {
        "UUID": str(uuid.uuid4()),
        "name": "RandomName",
        "value": 100  # Arbitrary fields for demonstration
    }
    collection.insert_one(document)
    return document["UUID"]

def find_document_by_uuid(uuid_str):
    return collection.find_one({"UUID": uuid_str})
