"""etcd connector using the etcd3 library."""

import os

import etcd3


def connect() -> etcd3.Etcd3Client:
    """Connect to etcd and return the client.

    Environment Variables:
        ETCD_HOST: etcd host (default: localhost)
        ETCD_PORT: etcd port (default: 2379)
    """
    host = os.environ.get('ETCD_HOST', 'localhost')
    port = int(os.environ.get('ETCD_PORT', '2379'))

    client = etcd3.client(
        host=host,
        port=port
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        version = client.status().version
        print(f"etcd version: {version}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to etcd: {e}")
