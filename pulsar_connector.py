from pulsar import Client

def connect():
    client = Client("pulsar://localhost:6650")
    return client

if __name__ == "__main__":
    client = connect()
    print(f"Apache Pulsar connected.")
    client.close()
