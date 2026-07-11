"""Pinecone vector database connector using pinecone-client v5+."""

import os

from pinecone import Pinecone


def connect() -> Pinecone:
    """Connect to Pinecone and return a client instance.

    Environment variables:
        PINECONE_API_KEY: Pinecone API key

    Returns:
        A Pinecone client instance.
    """
    api_key = os.environ.get("PINECONE_API_KEY", "<api-key>")
    pc = Pinecone(api_key=api_key)
    return pc


if __name__ == "__main__":
    try:
        pc = connect()
        indexes = pc.list_indexes()
        print(f"Pinecone connected. Indexes: {[idx.name for idx in indexes]}")
    except Exception as e:
        print(f"Failed to connect to Pinecone: {e}")
