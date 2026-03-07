from neo4j import GraphDatabase

def connect():
    driver = GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("<username>", "<password>")
    )
    return driver

if __name__ == "__main__":
    driver = connect()
    with driver.session() as session:
        result = session.run("CALL dbms.components() YIELD versions RETURN versions[0]")
        print(f"Neo4j version: {result.single()[0]}")
    driver.close()
