from dgraph import DgraphClient, DgraphClientStub

def connect():
    stub = DgraphClientStub("localhost:9080")
    client = DgraphClient(stub)
    return client

if __name__ == "__main__":
    client = connect()
    query = "{ q(func: has(name)) { uid } }"
    txn = client.txn(read_only=True)
    res = txn.query(query)
    print(f"Dgraph connected. Response: {res.json}")
    txn.discard()
