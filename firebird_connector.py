"""Firebird database connector using firebird-driver."""

import os

import firebird.driver


def connect() -> firebird.driver.Connection:
    """Connect to a Firebird database.

    Environment variables:
        FIREBIRD_HOST: Database host (default: localhost)
        FIREBIRD_DATABASE: Path to the database file
        FIREBIRD_USER: Database username (default: SYSDBA)
        FIREBIRD_PASSWORD: Database password

    Returns:
        A Firebird connection object.
    """
    conn = firebird.driver.connect(
        server=os.environ.get("FIREBIRD_HOST", "localhost"),
        database=os.environ.get("FIREBIRD_DATABASE", "<database-path>"),
        user=os.environ.get("FIREBIRD_USER", "SYSDBA"),
        password=os.environ.get("FIREBIRD_PASSWORD", "<password>"),
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT rdb$get_context('SYSTEM', 'ENGINE_VERSION') FROM rdb$database")
        print(f"Firebird version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Firebird: {e}")
