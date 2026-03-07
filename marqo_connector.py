import marqo

def connect():
    client = marqo.Client(url="http://localhost:8882")
    return client

if __name__ == "__main__":
    client = connect()
    health = client.health()
    print(f"Marqo connected. Health: {health}")
