import boto3

def connect():
    client = boto3.client(
        "neptune",
        region_name="<region>",
        aws_access_key_id="<access-key>",
        aws_secret_access_key="<secret-key>"
    )
    return client

if __name__ == "__main__":
    from gremlin_python.driver import client as gremlin_client
    gc = gremlin_client.Client(
        "wss://<cluster-endpoint>:8182/gremlin",
        "g"
    )
    result = gc.submit("g.V().count()").all().result()
    print(f"Neptune connected. Vertex count: {result}")
    gc.close()
