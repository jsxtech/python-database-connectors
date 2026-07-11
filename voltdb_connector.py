"""VoltDB connector using the VoltDB Python client.

Note: The VoltDB Python client is distributed with VoltDB and may need
to be installed from the VoltDB distribution rather than PyPI.
See: https://docs.voltdb.com/
"""

import os

import voltdb


def connect() -> voltdb.Client:
    """Connect to VoltDB and return the client.

    Environment Variables:
        VOLTDB_HOST: VoltDB host (default: localhost)
        VOLTDB_PORT: VoltDB client port (default: 21212)
    """
    host = os.environ.get('VOLTDB_HOST', 'localhost')
    port = int(os.environ.get('VOLTDB_PORT', '21212'))

    client = voltdb.Client()
    client.create_connection(host, port)
    return client


if __name__ == "__main__":
    try:
        client = connect()
        response = client.call_procedure("@SystemInformation", "OVERVIEW")
        print(f"VoltDB connected. Status: {response.status}")
        client.close()
    except Exception as e:
        print(f"Failed to connect to VoltDB: {e}")
