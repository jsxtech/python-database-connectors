"""Weaviate vector database connector using weaviate-client v4 API."""

import os

import weaviate
from weaviate.classes.init import Auth


def connect() -> weaviate.WeaviateClient:
    """Connect to Weaviate using v4 API.

    Environment variables:
        WEAVIATE_HOST: Weaviate server hostname (default: localhost)
        WEAVIATE_PORT: Weaviate HTTP port (default: 8080)
        WEAVIATE_API_KEY: API key for authentication (default: <api-key>)
    """
    host = os.environ.get('WEAVIATE_HOST', 'localhost')
    port = int(os.environ.get('WEAVIATE_PORT', '8080'))
    api_key = os.environ.get('WEAVIATE_API_KEY', '<api-key>')
    client = weaviate.connect_to_local(host=host, port=port)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        meta = client.get_meta()
        print(f"Weaviate version: {meta['version']}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Weaviate: {e}")
