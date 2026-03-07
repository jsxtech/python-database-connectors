import psycopg2

def connect():
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
    cursor.execute("SELECT version()")
    print(f"PostgreSQL version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
