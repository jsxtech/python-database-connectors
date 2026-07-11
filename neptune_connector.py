"""AWS Neptune connector using gremlin_python."""

import os

from gremlin_python.driver.client import Client


def connect() -> Client:
    """Connect to AWS Neptune via Gremlin.

    Environment variables:
        NEPTUNE_ENDPOINT: Neptune cluster endpoint
        NEPTUNE_PORT: Neptune port (default: 8182)
    """
    endpoint = os.environ.get('NEPTUNE_ENDPOINT', '<cluster-endpoint>')
    port = os.environ.get('NEPTUNE_PORT', '8182')
    client = Client(f'wss://{endpoint}:{port}/gremlin', 'g')
    return client


if __name__ == "__main__":
    try:
        client = connect()
        result = client.submit("g.V().count()").all().result()
        print(f"Neptune connected. Vertex count: {result}")
        client.close()
    except Exception as e:
        print(f"Error connecting to Neptune: {e}")
