"""Typesense connector using the typesense-python client."""

import os

import typesense


def connect() -> typesense.Client:
    """Connect to Typesense and return the client.

    Environment Variables:
        TYPESENSE_HOST: Typesense server host (default: localhost)
        TYPESENSE_PORT: Typesense server port (default: 8108)
        TYPESENSE_PROTOCOL: Connection protocol (default: http)
        TYPESENSE_API_KEY: API key for authentication
    """
    host = os.environ.get('TYPESENSE_HOST', 'localhost')
    port = os.environ.get('TYPESENSE_PORT', '8108')
    protocol = os.environ.get('TYPESENSE_PROTOCOL', 'http')
    api_key = os.environ.get('TYPESENSE_API_KEY', '<api-key>')

    client = typesense.Client({
        "nodes": [{"host": host, "port": port, "protocol": protocol}],
        "api_key": api_key,
        "connection_timeout_seconds": 2
    })
    return client


if __name__ == "__main__":
    try:
        client = connect()
        health = client.operations.is_healthy()
        print(f"Typesense connected. Healthy: {health}")
    except Exception as e:
        print(f"Failed to connect to Typesense: {e}")
