from qdrant_client import QdrantClient

def connect():
    client = QdrantClient(
        url="http://localhost:6333",
        api_key="<api-key>"
    )
    return client

if __name__ == "__main__":
    client = connect()
    collections = client.get_collections()
    print(f"Qdrant connected. Collections: {collections}")
