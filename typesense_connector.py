import typesense

def connect():
    client = typesense.Client({
        "nodes": [{"host": "localhost", "port": "8108", "protocol": "http"}],
        "api_key": "<api-key>",
        "connection_timeout_seconds": 2
    })
    return client

if __name__ == "__main__":
    client = connect()
    health = client.operations.is_healthy()
    print(f"Typesense connected. Healthy: {health}")
