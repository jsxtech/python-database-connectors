"""QuestDB connector using psycopg2 for queries and questdb.ingress for data ingestion."""

import os

import psycopg2


def connect() -> psycopg2.extensions.connection:
    """Connect to QuestDB via PostgreSQL wire protocol and return the connection.

    Environment Variables:
        QUESTDB_HOST: QuestDB host (default: localhost)
        QUESTDB_PORT: QuestDB PostgreSQL wire port (default: 8812)
        QUESTDB_USER: Database username (default: admin)
        QUESTDB_PASSWORD: Database password (default: quest)
        QUESTDB_DATABASE: Database name (default: qdb)
    """
    host = os.environ.get('QUESTDB_HOST', 'localhost')
    port = int(os.environ.get('QUESTDB_PORT', '8812'))
    user = os.environ.get('QUESTDB_USER', 'admin')
    password = os.environ.get('QUESTDB_PASSWORD', 'quest')
    database = os.environ.get('QUESTDB_DATABASE', 'qdb')

    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        print(f"QuestDB connected. Test query: {cursor.fetchone()}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to QuestDB: {e}")
