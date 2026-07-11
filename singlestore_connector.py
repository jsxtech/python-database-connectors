"""SingleStore database connector."""

import os

import singlestoredb


def connect() -> singlestoredb.Connection:
    """Connect to a SingleStore database.

    Environment variables:
        SINGLESTORE_HOST: Database host
        SINGLESTORE_PORT: Database port (default: 3306)
        SINGLESTORE_USER: Database username
        SINGLESTORE_PASSWORD: Database password
        SINGLESTORE_DATABASE: Database name

    Returns:
        A SingleStore connection object.
    """
    conn = singlestoredb.connect(
        host=os.environ.get("SINGLESTORE_HOST", "<host>"),
        port=int(os.environ.get("SINGLESTORE_PORT", "3306")),
        user=os.environ.get("SINGLESTORE_USER", "<username>"),
        password=os.environ.get("SINGLESTORE_PASSWORD", "<password>"),
        database=os.environ.get("SINGLESTORE_DATABASE", "<database>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT @@version")
        print(f"SingleStore version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to SingleStore: {e}")
