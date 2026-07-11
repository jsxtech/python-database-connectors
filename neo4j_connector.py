"""Neo4j connector using neo4j Python driver."""

import os

from neo4j import GraphDatabase, Driver


def connect() -> Driver:
    """Connect to Neo4j.

    Environment variables:
        NEO4J_URI: Neo4j Bolt URI (default: bolt://localhost:7687)
        NEO4J_USERNAME: Authentication username (default: <username>)
        NEO4J_PASSWORD: Authentication password (default: <password>)
    """
    uri = os.environ.get('NEO4J_URI', 'bolt://localhost:7687')
    username = os.environ.get('NEO4J_USERNAME', '<username>')
    password = os.environ.get('NEO4J_PASSWORD', '<password>')
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver


if __name__ == "__main__":
    try:
        driver = connect()
        with driver.session() as session:
            result = session.run("CALL dbms.components() YIELD versions RETURN versions[0]")
            print(f"Neo4j version: {result.single()[0]}")
        driver.close()
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}")
