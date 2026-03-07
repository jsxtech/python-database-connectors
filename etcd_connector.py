import etcd3

def connect():
    client = etcd3.client(
        host="localhost",
        port=2379
    )
    return client

if __name__ == "__main__":
    client = connect()
    version = client.status().version
    print(f"etcd version: {version}")
