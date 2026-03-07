from scylla_driver import Cluster

def connect():
    cluster = Cluster(["localhost"])
    session = cluster.connect()
    return session

if __name__ == "__main__":
    session = connect()
    result = session.execute("SELECT release_version FROM system.local")
    print(f"ScyllaDB version: {result.one()[0]}")
    session.shutdown()
