from pymongo import MongoClient
from django.conf import settings

def get_task_collection():
    """
    Returns the MongoDB collection used to store task documents.

    This function creates a MongoDB client using the connection URI
    defined in Django settings, selects the configured database,
    and returns the 'tasks' collection.

    Returns:
        pymongo.collection.Collection: MongoDB 'tasks' collection instance.
    """
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB_NAME]
    return db["tasks"]
