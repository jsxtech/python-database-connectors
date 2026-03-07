from faunadb import query as q
from faunadb.client import FaunaClient

def connect():
    client = FaunaClient(secret="<secret-key>")
    return client

if __name__ == "__main__":
    client = connect()
    result = client.query(q.paginate(q.databases()))
    print(f"Fauna connected. Databases: {result}")
