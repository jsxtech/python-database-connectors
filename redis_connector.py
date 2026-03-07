import redis

def connect():
    client = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )
    return client

if __name__ == "__main__":
    client = connect()
    client.ping()
    print(f"Redis connected. Server info: {client.info('server')['redis_version']}")
    client.close()
