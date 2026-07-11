"""TigerGraph connector using pyTigerGraph."""

import os

import pyTigerGraph as tg


def connect() -> tg.TigerGraphConnection:
    """Connect to TigerGraph.

    Environment variables:
        TIGERGRAPH_HOST: TigerGraph server URL (default: http://localhost)
        TIGERGRAPH_GRAPHNAME: Graph name
        TIGERGRAPH_USERNAME: Authentication username
        TIGERGRAPH_PASSWORD: Authentication password
    """
    host = os.environ.get("TIGERGRAPH_HOST", "http://localhost")
    graphname = os.environ.get("TIGERGRAPH_GRAPHNAME", "<graph>")
    username = os.environ.get("TIGERGRAPH_USERNAME", "<username>")
    password = os.environ.get("TIGERGRAPH_PASSWORD", "<password>")

    conn = tg.TigerGraphConnection(
        host=host,
        graphname=graphname,
        username=username,
        password=password,
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        version = conn.getVersion()
        print(f"TigerGraph version: {version}")
    except Exception as e:
        print(f"Failed to connect to TigerGraph: {e}")
