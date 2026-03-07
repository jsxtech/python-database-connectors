import meilisearch

def connect():
    client = meilisearch.Client("http://localhost:7700", "<api-key>")
    return client

if __name__ == "__main__":
    client = connect()
    health = client.health()
    print(f"Meilisearch connected. Health: {health}")
