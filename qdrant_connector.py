"""Qdrant vector database connector using qdrant-client."""

import os

from qdrant_client import QdrantClient


def connect() -> QdrantClient:
    """Connect to Qdrant.

    Environment variables:
        QDRANT_HOST: Qdrant server hostname (default: localhost)
        QDRANT_PORT: Qdrant HTTP port (default: 6333)
        QDRANT_API_KEY: API key for authentication (default: <api-key>)
    """
    host = os.environ.get('QDRANT_HOST', 'localhost')
    port = int(os.environ.get('QDRANT_PORT', '6333'))
    api_key = os.environ.get('QDRANT_API_KEY', '<api-key>')
    client = QdrantClient(
        url=f"http://{host}:{port}",
        api_key=api_key if api_key != '<api-key>' else None
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        collections = client.get_collections()
        print(f"Qdrant connected. Collections: {collections}")
    except Exception as e:
        print(f"Failed to connect to Qdrant: {e}")
