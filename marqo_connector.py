"""Marqo vector search connector using marqo."""

import os

import marqo


def connect() -> marqo.Client:
    """Connect to Marqo.

    Environment variables:
        MARQO_HOST: Marqo server hostname (default: localhost)
        MARQO_PORT: Marqo server port (default: 8882)
    """
    host = os.environ.get('MARQO_HOST', 'localhost')
    port = os.environ.get('MARQO_PORT', '8882')
    client = marqo.Client(url=f"http://{host}:{port}")
    return client


if __name__ == "__main__":
    try:
        client = connect()
        health = client.health()
        print(f"Marqo connected. Health: {health}")
    except Exception as e:
        print(f"Failed to connect to Marqo: {e}")
