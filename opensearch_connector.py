from opensearchpy import OpenSearch

def connect():
    client = OpenSearch(
        hosts=[{"host": "localhost", "port": 9200}],
        http_auth=("<username>", "<password>"),
        use_ssl=False
    )
    return client

if __name__ == "__main__":
    client = connect()
    info = client.info()
    print(f"OpenSearch version: {info['version']['number']}")
