"""Redis connector using redis-py."""

import os

import redis


def connect() -> redis.Redis:
    """Connect to Redis.

    Environment variables:
        REDIS_HOST: Redis server hostname (default: localhost)
        REDIS_PORT: Redis server port (default: 6379)
        REDIS_PASSWORD: Redis password (default: empty)
    """
    host = os.environ.get('REDIS_HOST', 'localhost')
    port = int(os.environ.get('REDIS_PORT', '6379'))
    password = os.environ.get('REDIS_PASSWORD', '')
    client = redis.Redis(
        host=host,
        port=port,
        password=password or None,
        decode_responses=True
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        client.ping()
        print(f"Redis connected. Server info: {client.info('server')['redis_version']}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
