"""Nebula Graph connector using nebula3-python."""

import os

from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config


def connect() -> ConnectionPool:
    """Connect to Nebula Graph.

    Environment variables:
        NEBULA_HOST: Nebula Graph server hostname (default: localhost)
        NEBULA_PORT: Nebula Graph port (default: 9669)
        NEBULA_USERNAME: Authentication username (default: <username>)
        NEBULA_PASSWORD: Authentication password (default: <password>)
    """
    host = os.environ.get('NEBULA_HOST', 'localhost')
    port = int(os.environ.get('NEBULA_PORT', '9669'))
    config = Config()
    connection_pool = ConnectionPool()
    connection_pool.init([(host, port)], config)
    return connection_pool


if __name__ == "__main__":
    try:
        pool = connect()
        username = os.environ.get('NEBULA_USERNAME', '<username>')
        password = os.environ.get('NEBULA_PASSWORD', '<password>')
        session = pool.get_session(username, password)
        result = session.execute("SHOW HOSTS")
        print(f"NebulaGraph connected. Result: {result}")
        session.release()
        pool.close()
    except Exception as e:
        print(f"Failed to connect to Nebula Graph: {e}")
