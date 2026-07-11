"""Azure Cosmos DB connector using azure-cosmos."""

import os

from azure.cosmos import CosmosClient


def connect() -> CosmosClient:
    """Connect to Azure Cosmos DB.

    Environment variables:
        COSMOSDB_URL: Cosmos DB account URL (e.g., https://<account>.documents.azure.com:443/)
        COSMOSDB_KEY: Cosmos DB account key
    """
    client = CosmosClient(
        url=os.environ.get('COSMOSDB_URL', 'https://<account>.documents.azure.com:443/'),
        credential=os.environ.get('COSMOSDB_KEY', '<key>')
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        databases = list(client.list_databases())
        print(f"Cosmos DB connected. Databases: {[db['id'] for db in databases]}")
    except Exception as e:
        print(f"Error connecting to Cosmos DB: {e}")
