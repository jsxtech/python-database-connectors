"""Apache Cassandra connector using cassandra-driver."""

import os

from cassandra.cluster import Cluster, Session
from cassandra.auth import PlainTextAuthProvider


def connect() -> Session:
    """Connect to Cassandra.

    Environment variables:
        CASSANDRA_HOST: Cassandra contact point (default: localhost)
        CASSANDRA_PORT: Cassandra native transport port (default: 9042)
        CASSANDRA_USERNAME: Authentication username (default: <username>)
        CASSANDRA_PASSWORD: Authentication password (default: <password>)
    """
    host = os.environ.get('CASSANDRA_HOST', 'localhost')
    port = int(os.environ.get('CASSANDRA_PORT', '9042'))
    username = os.environ.get('CASSANDRA_USERNAME', '<username>')
    password = os.environ.get('CASSANDRA_PASSWORD', '<password>')
    auth_provider = PlainTextAuthProvider(username=username, password=password)
    cluster = Cluster([host], port=port, auth_provider=auth_provider)
    session = cluster.connect()
    return session


if __name__ == "__main__":
    try:
        session = connect()
        result = session.execute("SELECT release_version FROM system.local")
        print(f"Cassandra version: {result.one()[0]}")
        session.shutdown()
    except Exception as e:
        print(f"Failed to connect to Cassandra: {e}")
