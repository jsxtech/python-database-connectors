from azure.cosmos import CosmosClient

def connect():
    client = CosmosClient(
        url="https://<account>.documents.azure.com:443/",
        credential="<key>"
    )
    return client

if __name__ == "__main__":
    client = connect()
    databases = list(client.list_databases())
    print(f"Cosmos DB connected. Databases: {[db['id'] for db in databases]}")
