import psycopg2

def connect():
    conn = psycopg2.connect(
        host="<host>",
        user="<username>",
        password="<password>",
        database="<database>",
        port=26257,
        sslmode="require"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"CockroachDB version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
