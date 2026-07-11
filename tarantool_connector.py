"""Tarantool connector using the tarantool-python library."""

import os

import tarantool


def connect() -> tarantool.Connection:
    """Connect to Tarantool and return the connection.

    Environment Variables:
        TARANTOOL_HOST: Tarantool host (default: localhost)
        TARANTOOL_PORT: Tarantool port (default: 3301)
        TARANTOOL_USER: Authentication username
        TARANTOOL_PASSWORD: Authentication password
    """
    host = os.environ.get('TARANTOOL_HOST', 'localhost')
    port = int(os.environ.get('TARANTOOL_PORT', '3301'))
    user = os.environ.get('TARANTOOL_USER', '<username>')
    password = os.environ.get('TARANTOOL_PASSWORD', '<password>')

    conn = tarantool.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        result = conn.eval("return box.info.version")
        print(f"Tarantool version: {result[0]}")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Tarantool: {e}")
