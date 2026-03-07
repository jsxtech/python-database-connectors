import happybase

def connect():
    conn = happybase.Connection(host="localhost", port=9090)
    return conn

if __name__ == "__main__":
    conn = connect()
    tables = conn.tables()
    print(f"HBase connected. Tables: {tables}")
    conn.close()
