import milvus

def connect():
    from pymilvus import connections
    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )
    return connections

if __name__ == "__main__":
    conn = connect()
    from pymilvus import utility
    print(f"Milvus connected. Collections: {utility.list_collections()}")
