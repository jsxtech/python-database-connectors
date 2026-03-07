import edgedb

def connect():
    client = edgedb.create_client(
        host="localhost",
        port=5656,
        user="<username>",
        password="<password>",
        database="<database>"
    )
    return client

if __name__ == "__main__":
    client = connect()
    result = client.query("SELECT sys::get_version_as_str()")
    print(f"EdgeDB version: {result[0]}")
    client.close()
