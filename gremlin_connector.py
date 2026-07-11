"""Gremlin connector using gremlinpython."""

import os

from gremlin_python.driver import client


def connect() -> client.Client:
    """Connect to a Gremlin-compatible graph database.

    Environment variables:
        GREMLIN_HOST: Gremlin server hostname (default: localhost)
        GREMLIN_PORT: Gremlin WebSocket port (default: 8182)
    """
    host = os.environ.get('GREMLIN_HOST', 'localhost')
    port = os.environ.get('GREMLIN_PORT', '8182')
    url = f"ws://{host}:{port}/gremlin"
    gremlin_client = client.Client(url, "g")
    return gremlin_client


if __name__ == "__main__":
    try:
        gremlin_client = connect()
        result = gremlin_client.submit("g.V().count()").all().result()
        print(f"Gremlin connected. Vertex count: {result}")
        gremlin_client.close()
    except Exception as e:
        print(f"Failed to connect to Gremlin server: {e}")
