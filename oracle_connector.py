"""Oracle database connector."""

import os

import oracledb


def connect() -> oracledb.Connection:
    """Connect to an Oracle database.

    Environment variables:
        ORACLE_USER: Database username
        ORACLE_PASSWORD: Database password
        ORACLE_HOST: Database host (default: localhost)
        ORACLE_PORT: Database port (default: 1521)
        ORACLE_SERVICE: Oracle service name

    Returns:
        An Oracle connection object.
    """
    host = os.environ.get("ORACLE_HOST", "localhost")
    port = os.environ.get("ORACLE_PORT", "1521")
    service = os.environ.get("ORACLE_SERVICE", "<service_name>")
    conn = oracledb.connect(
        user=os.environ.get("ORACLE_USER", "<username>"),
        password=os.environ.get("ORACLE_PASSWORD", "<password>"),
        dsn=f"{host}:{port}/{service}",
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT banner FROM v$version WHERE banner LIKE 'Oracle%'")
        print(f"Oracle version: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to Oracle: {e}")
