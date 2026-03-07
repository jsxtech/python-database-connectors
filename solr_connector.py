import pysolr

def connect():
    solr = pysolr.Solr("http://localhost:8983/solr/<core>")
    return solr

if __name__ == "__main__":
    solr = connect()
    print(f"Solr connected. Ping: {solr.ping()}")
