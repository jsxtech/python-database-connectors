"""Meilisearch connector using the meilisearch-python client."""

import os

import meilisearch


def connect() -> meilisearch.Client:
    """Connect to Meilisearch and return the client.

    Environment Variables:
        MEILISEARCH_URL: Meilisearch server URL (default: http://localhost:7700)
        MEILISEARCH_API_KEY: API key for authentication
    """
    url = os.environ.get('MEILISEARCH_URL', 'http://localhost:7700')
    api_key = os.environ.get('MEILISEARCH_API_KEY', '<api-key>')

    client = meilisearch.Client(url, api_key)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        health = client.health()
        print(f"Meilisearch connected. Health: {health}")
    except Exception as e:
        print(f"Failed to connect to Meilisearch: {e}")
