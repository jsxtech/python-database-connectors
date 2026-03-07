from pymemcache.client import base

def connect():
    client = base.Client(("localhost", 11211))
    return client

if __name__ == "__main__":
    client = connect()
    client.set("test", "connected")
    result = client.get("test")
    print(f"Memcached connected. Test value: {result.decode()}")
    client.close()
