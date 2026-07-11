"""Dgraph connector using pydgraph."""

import os

from pydgraph import DgraphClient, DgraphClientStub


def connect() -> DgraphClient:
    """Connect to Dgraph.

    Environment variables:
        DGRAPH_HOST: Dgraph server hostname (default: localhost)
        DGRAPH_PORT: Dgraph gRPC port (default: 9080)
    """
    host = os.environ.get('DGRAPH_HOST', 'localhost')
    port = os.environ.get('DGRAPH_PORT', '9080')
    stub = DgraphClientStub(f"{host}:{port}")
    client = DgraphClient(stub)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        query = "{ q(func: has(name)) { uid } }"
        txn = client.txn(read_only=True)
        res = txn.query(query)
        print(f"Dgraph connected. Response: {res.json}")
        txn.discard()
    except Exception as e:
        print(f"Failed to connect to Dgraph: {e}")
