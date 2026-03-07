from rockset import RocksetClient

def connect():
    client = RocksetClient(api_key="<api-key>", api_server="<region>.rockset.com")
    return client

if __name__ == "__main__":
    client = connect()
    workspaces = client.Workspaces.list()
    print(f"Rockset connected. Workspaces: {[w.name for w in workspaces.data]}")
