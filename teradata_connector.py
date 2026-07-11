"""Teradata database connector."""

import os

import teradatasql


def connect() -> teradatasql.TeradataConnection:
    """Connect to a Teradata database.

    Environment variables:
        TERADATA_HOST: Database host
        TERADATA_USER: Database username
        TERADATA_PASSWORD: Database password

    Returns:
        A Teradata connection object.
    """
    conn = teradatasql.connect(
        host=os.environ.get("TERADATA_HOST", "<host>"),
        user=os.environ.get("TERADATA_USER", "<username>"),
        password=os.environ.get("TERADATA_PASSWORD", "<password>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT InfoData FROM DBC.DBCInfoV WHERE InfoKey = 'VERSION'")
        print(f"Teradata version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Teradata: {e}")
