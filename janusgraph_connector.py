from janusgraph_python import JanusGraph

def connect():
    graph = JanusGraph("localhost", 8182)
    return graph

if __name__ == "__main__":
    from gremlin_python.driver import client
    gremlin_client = client.Client("ws://localhost:8182/gremlin", "g")
    result = gremlin_client.submit("g.V().count()").all().result()
    print(f"JanusGraph connected. Vertex count: {result}")
    gremlin_client.close()
