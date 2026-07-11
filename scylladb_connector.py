"""ScyllaDB connector using scylla-driver."""

import os

from cassandra.cluster import Session
from scylla_driver import Cluster


def connect() -> Session:
    """Connect to ScyllaDB.

    Environment variables:
        SCYLLADB_HOST: ScyllaDB contact point (default: localhost)
        SCYLLADB_PORT: ScyllaDB native transport port (default: 9042)
    """
    host = os.environ.get('SCYLLADB_HOST', 'localhost')
    port = int(os.environ.get('SCYLLADB_PORT', '9042'))
    cluster = Cluster([host], port=port)
    session = cluster.connect()
    return session


if __name__ == "__main__":
    try:
        session = connect()
        result = session.execute("SELECT release_version FROM system.local")
        print(f"ScyllaDB version: {result.one()[0]}")
        session.shutdown()
    except Exception as e:
        print(f"Failed to connect to ScyllaDB: {e}")
