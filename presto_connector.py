import prestodb

def connect():
    conn = prestodb.dbapi.connect(
        host="localhost",
        port=8080,
        user="<username>",
        catalog="<catalog>",
        schema="<schema>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(f"Presto version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
