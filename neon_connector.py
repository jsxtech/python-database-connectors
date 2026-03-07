import psycopg2

def connect():
    conn = psycopg2.connect(
        host="<project-id>.neon.tech",
        user="<username>",
        password="<password>",
        database="<database>",
        sslmode="require"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"Neon version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
