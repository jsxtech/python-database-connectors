"""JanusGraph connector using Gremlin Python driver."""

import os

from gremlin_python.driver import client as gremlin_client


def connect() -> gremlin_client.Client:
    """Connect to JanusGraph via Gremlin WebSocket.

    Environment variables:
        JANUSGRAPH_HOST: JanusGraph server hostname (default: localhost)
        JANUSGRAPH_PORT: JanusGraph Gremlin port (default: 8182)
    """
    host = os.environ.get('JANUSGRAPH_HOST', 'localhost')
    port = os.environ.get('JANUSGRAPH_PORT', '8182')
    url = f"ws://{host}:{port}/gremlin"
    connection = gremlin_client.Client(url, "g")
    return connection


if __name__ == "__main__":
    try:
        connection = connect()
        result = connection.submit("g.V().count()").all().result()
        print(f"JanusGraph connected. Vertex count: {result}")
        connection.close()
    except Exception as e:
        print(f"Failed to connect to JanusGraph: {e}")
