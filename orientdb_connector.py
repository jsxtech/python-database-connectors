from orientdb import OrientDB

def connect():
    client = OrientDB(host="localhost", port=2424)
    session_id = client.connect("<username>", "<password>")
    db = client.db_open("<database>", "<username>", "<password>")
    return client

if __name__ == "__main__":
    client = connect()
    print(f"OrientDB connected. Session ID: {client}")
    client.db_close()
