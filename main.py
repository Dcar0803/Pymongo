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

def save_document(document):

    """Save a given document to the MongoDB collection.

    Args:
        document (dict): The document to save
    """
    collection.insert_one(document)

def find_document_by_uuid(uuid_str):#Third function

    """
    Find a MongoDB document by its UUID.

    Args:
        uuid_str (str): The UUID of the document to find

    Returns:
        dict: The found document or None
    """
    return collection.find_one({"UUID": uuid_str})


def update_document_field(uuid_str, field, value):

    """ Update a specific field in a MongoDB document with a specified UUID.

    Args:
        uuid_str (str): The UUID of the document to update
        field (str): The field to update
        value: The new value for the field
    """

    collection.update_one({"UUID": uuid_str}, {"$set": {field: value}})


def delete_document_by_uuid(uuid_str):

    """
    Delete a MongoDB document by its UUID.

    Args:
        uuid_str (str): The UUID of the document to delete
    """
    
    collection.delete_one({"UUID": uuid_str})