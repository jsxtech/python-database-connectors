from singlestoredb import connect as singlestore_connect

def connect():
    conn = singlestore_connect(
        host="<host>",
        port=3306,
        user="<username>",
        password="<password>",
        database="<database>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT @@version")
    print(f"SingleStore version: {cursor.fetchone()[0]}")
    cursor.close()
    conn.close()
