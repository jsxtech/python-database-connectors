from gremlin_python.driver import client

def connect():
    gremlin_client = client.Client(
        "ws://localhost:8182/gremlin",
        "g"
    )
    return gremlin_client

if __name__ == "__main__":
    gremlin_client = connect()
    result = gremlin_client.submit("g.V().count()").all().result()
    print(f"Gremlin connected. Vertex count: {result}")
    gremlin_client.close()
