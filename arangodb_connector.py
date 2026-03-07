from arango import ArangoClient

def connect():
    client = ArangoClient(hosts="http://localhost:8529")
    db = client.db("<database>", username="<username>", password="<password>")
    return db

if __name__ == "__main__":
    db = connect()
    version = db.version()
    print(f"ArangoDB version: {version}")
