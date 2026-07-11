"""Valkey connector using the redis-py library (Redis-compatible)."""

import os

import redis


def connect() -> redis.Redis:
    """Connect to Valkey and return a Redis client.

    Valkey is Redis-compatible, so the standard redis-py client is used.

    Environment Variables:
        VALKEY_HOST: Valkey host (default: localhost)
        VALKEY_PORT: Valkey port (default: 6379)
        VALKEY_PASSWORD: Authentication password (optional)
    """
    host = os.environ.get('VALKEY_HOST', 'localhost')
    port = int(os.environ.get('VALKEY_PORT', '6379'))
    password = os.environ.get('VALKEY_PASSWORD', None)

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
        print(f"Valkey connected. Server info: {client.info('server')}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Valkey: {e}")
