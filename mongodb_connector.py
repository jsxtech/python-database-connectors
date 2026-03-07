from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb://localhost:27017/")
    return client

if __name__ == "__main__":
    client = connect()
    db = client["<database>"]
    print(f"MongoDB connected. Databases: {client.list_database_names()}")
    client.close()
