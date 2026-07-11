"""RDF triplestore reader using the rdflib library.

Note: This is a file format reader, not a database connection.
It parses RDF (Resource Description Framework) files into an in-memory graph.
"""

import os

from rdflib import Graph


def connect() -> Graph:
    """Parse an RDF file and return an rdflib Graph.

    Note: This is a file reader, not a database connection.

    Environment Variables:
        RDF_FILE: Path to the RDF file to parse
    """
    filepath = os.environ.get('RDF_FILE', '<file>.rdf')

    g = Graph()
    g.parse(filepath)
    return g


if __name__ == "__main__":
    try:
        g = connect()
        print(f"RDF Graph loaded. Triples: {len(g)}")
    except Exception as e:
        print(f"Failed to read RDF file: {e}")
