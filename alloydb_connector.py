import psycopg2

def connect():
    conn = psycopg2.connect(
        host="<alloydb-instance-ip>",
        user="<username>",
        password="<password>",
        database="<database>",
        port=5432
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"AlloyDB version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
