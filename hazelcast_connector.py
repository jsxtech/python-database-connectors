"""Hazelcast connector using the hazelcast-python-client library."""

import os

import hazelcast


def connect() -> hazelcast.HazelcastClient:
    """Connect to Hazelcast and return the client.

    Environment Variables:
        HAZELCAST_CLUSTER_MEMBERS: Comma-separated cluster member addresses (default: localhost:5701)
    """
    members = os.environ.get('HAZELCAST_CLUSTER_MEMBERS', 'localhost:5701')

    client = hazelcast.HazelcastClient(
        cluster_members=members.split(',')
    )
    return client


if __name__ == "__main__":
    try:
        client = connect()
        print(f"Hazelcast connected. Cluster: {client.cluster_service}")
        client.shutdown()
    except Exception as e:
        print(f"Failed to connect to Hazelcast: {e}")
