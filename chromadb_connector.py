import chromadb

def connect():
    client = chromadb.Client()
    return client

if __name__ == "__main__":
    client = connect()
    collections = client.list_collections()
    print(f"ChromaDB connected. Collections: {[c.name for c in collections]}")
