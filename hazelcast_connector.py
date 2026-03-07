import hazelcast

def connect():
    client = hazelcast.HazelcastClient(
        cluster_members=["localhost:5701"]
    )
    return client

if __name__ == "__main__":
    client = connect()
    print(f"Hazelcast connected. Cluster: {client.cluster_service}")
    client.shutdown()
