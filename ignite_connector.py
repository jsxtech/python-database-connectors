"""Apache Ignite connector using the pyignite library."""

import os

from pyignite import Client


def connect() -> Client:
    """Connect to Apache Ignite and return the client.

    Environment Variables:
        IGNITE_HOST: Ignite node host (default: localhost)
        IGNITE_PORT: Ignite thin client port (default: 10800)
    """
    host = os.environ.get('IGNITE_HOST', 'localhost')
    port = int(os.environ.get('IGNITE_PORT', '10800'))

    client = Client()
    client.connect(host, port)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        print(f"Apache Ignite connected. Protocol version: {client.protocol_version}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Apache Ignite: {e}")
