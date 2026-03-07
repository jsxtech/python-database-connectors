import clickhouse_connect

def connect():
    client = clickhouse_connect.get_client(
        host="localhost",
        port=8123,
        username="<username>",
        password="<password>"
    )
    return client

if __name__ == "__main__":
    client = connect()
    result = client.query("SELECT version()")
    print(f"ClickHouse version: {result.result_rows[0][0]}")
