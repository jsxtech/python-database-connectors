import tarantool

def connect():
    conn = tarantool.connect(
        host="localhost",
        port=3301,
        user="<username>",
        password="<password>"
    )
    return conn

if __name__ == "__main__":
    conn = connect()
    result = conn.eval("return box.info.version")
    print(f"Tarantool version: {result[0]}")
    conn.close()
