from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

def connect():
    auth = PasswordAuthenticator("<username>", "<password>")
    cluster = Cluster("couchbase://localhost", authenticator=auth)
    return cluster

if __name__ == "__main__":
    cluster = connect()
    bucket = cluster.bucket("<bucket>")
    print(f"Couchbase connected. Bucket: {bucket.name}")
