"""Apache Pulsar connector using the pulsar-client library."""

import os

from pulsar import Client


def connect() -> Client:
    """Connect to Apache Pulsar and return the client.

    Environment Variables:
        PULSAR_URL: Pulsar service URL (default: pulsar://localhost:6650)
    """
    url = os.environ.get('PULSAR_URL', 'pulsar://localhost:6650')

    client = Client(url)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        print("Apache Pulsar connected.")
        client.close()
    except Exception as e:
        print(f"Failed to connect to Apache Pulsar: {e}")
