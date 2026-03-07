import timescaledb

def connect():
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        user="<username>",
        password="<password>",
        database="<database>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT extversion FROM pg_extension WHERE extname = 'timescaledb'")
    print(f"TimescaleDB version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
