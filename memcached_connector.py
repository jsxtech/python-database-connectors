"""Memcached connector using the pymemcache library."""

import os

from pymemcache.client import base


def connect() -> base.Client:
    """Connect to Memcached and return the client.

    Environment Variables:
        MEMCACHED_HOST: Memcached host (default: localhost)
        MEMCACHED_PORT: Memcached port (default: 11211)
    """
    host = os.environ.get('MEMCACHED_HOST', 'localhost')
    port = int(os.environ.get('MEMCACHED_PORT', '11211'))

    client = base.Client((host, port))
    return client


if __name__ == "__main__":
    try:
        client = connect()
        client.set("test", "connected")
        result = client.get("test")
        print(f"Memcached connected. Test value: {result.decode()}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Memcached: {e}")
