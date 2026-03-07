import weaviate

def connect():
    client = weaviate.Client(
        url="http://localhost:8080",
        auth_client_secret=weaviate.AuthApiKey(api_key="<api-key>")
    )
    return client

if __name__ == "__main__":
    client = connect()
    meta = client.get_meta()
    print(f"Weaviate version: {meta['version']}")
