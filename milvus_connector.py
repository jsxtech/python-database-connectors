"""Milvus vector database connector using pymilvus."""

import os

from pymilvus import connections, utility


def connect() -> str:
    """Connect to Milvus and return the connection alias.

    Pymilvus uses a global connection registry. The returned alias can be
    used with other pymilvus APIs to reference this connection.

    Environment variables:
        MILVUS_HOST: Milvus server hostname (default: localhost)
        MILVUS_PORT: Milvus gRPC port (default: 19530)
        MILVUS_ALIAS: Connection alias (default: default)

    Returns:
        The connection alias string.
    """
    host = os.environ.get("MILVUS_HOST", "localhost")
    port = int(os.environ.get("MILVUS_PORT", "19530"))
    alias = os.environ.get("MILVUS_ALIAS", "default")
    connections.connect(
        alias=alias,
        host=host,
        port=port,
    )
    return alias


if __name__ == "__main__":
    try:
        alias = connect()
        print(f"Milvus connected (alias: {alias}). Collections: {utility.list_collections()}")
        connections.disconnect(alias)
    except Exception as e:
        print(f"Failed to connect to Milvus: {e}")
