"""ChromaDB vector database connector using chromadb."""

import os

import chromadb


def connect() -> chromadb.ClientAPI:
    """Connect to ChromaDB.

    Environment variables:
        CHROMADB_HOST: ChromaDB server hostname (default: localhost)
        CHROMADB_PORT: ChromaDB server port (default: 8000)
    """
    host = os.environ.get('CHROMADB_HOST', 'localhost')
    port = int(os.environ.get('CHROMADB_PORT', '8000'))
    client = chromadb.HttpClient(host=host, port=port)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        collections = client.list_collections()
        print(f"ChromaDB connected. Collections: {collections}")
    except Exception as e:
        print(f"Failed to connect to ChromaDB: {e}")
