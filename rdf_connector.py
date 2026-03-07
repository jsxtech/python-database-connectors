from rdflib import Graph

def connect():
    g = Graph()
    g.parse("<file>.rdf")
    return g

if __name__ == "__main__":
    g = connect()
    print(f"RDF Graph loaded. Triples: {len(g)}")
