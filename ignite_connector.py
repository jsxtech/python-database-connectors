import pyignite

def connect():
    from pyignite import Client
    client = Client()
    client.connect("localhost", 10800)
    return client

if __name__ == "__main__":
    client = connect()
    print(f"Apache Ignite connected. Protocol version: {client.protocol_version}")
    client.close()
