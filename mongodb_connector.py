"""MongoDB connector using pymongo."""

import os

from pymongo import MongoClient


def connect() -> MongoClient:
    """Connect to MongoDB.

    Environment variables:
        MONGODB_URI: MongoDB connection URI (default: mongodb://localhost:27017/)
        MONGODB_DATABASE: Database name (used in example)
    """
    uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
    client = MongoClient(uri)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        db = client[os.environ.get('MONGODB_DATABASE', '<database>')]
        print(f"MongoDB connected. Databases: {client.list_database_names()}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
