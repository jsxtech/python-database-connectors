"""Dragonfly connector using the redis-py library (Redis-compatible)."""

import os

import redis


def connect() -> redis.Redis:
    """Connect to Dragonfly and return a Redis client.

    Dragonfly is Redis-compatible, so the standard redis-py client is used.

    Environment Variables:
        DRAGONFLY_HOST: Dragonfly host (default: localhost)
        DRAGONFLY_PORT: Dragonfly port (default: 6379)
        DRAGONFLY_PASSWORD: Authentication password (optional)
    """
    host = os.environ.get('DRAGONFLY_HOST', 'localhost')
    port = int(os.environ.get('DRAGONFLY_PORT', '6379'))
    password = os.environ.get('DRAGONFLY_PASSWORD', None)

    client = redis.Redis(
        host=host,
        port=port,
        password=password,
        decode_responses=True
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        client.ping()
        print(f"Dragonfly connected. Info: {client.info()}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Dragonfly: {e}")
