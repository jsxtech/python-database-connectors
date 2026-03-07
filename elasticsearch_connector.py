from elasticsearch import Elasticsearch

def connect():
    client = Elasticsearch(
        ["http://localhost:9200"],
        basic_auth=("<username>", "<password>")
    )
    return client

if __name__ == "__main__":
    client = connect()
    info = client.info()
    print(f"Elasticsearch version: {info['version']['number']}")
