import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connect():
    auth_provider = PlainTextAuthProvider(username="<username>", password="<password>")
    cluster = Cluster(["localhost"], auth_provider=auth_provider)
    session = cluster.connect()
    return session

if __name__ == "__main__":
    session = connect()
    result = session.execute("SELECT release_version FROM system.local")
    print(f"Cassandra version: {result.one()[0]}")
    session.shutdown()
