from voltdb import FastSerializer

def connect():
    import voltdb
    client = voltdb.Client()
    client.create_connection("localhost", 21212)
    return client

if __name__ == "__main__":
    client = connect()
    response = client.call_procedure("@SystemInformation", "OVERVIEW")
    print(f"VoltDB connected. Status: {response.status}")
