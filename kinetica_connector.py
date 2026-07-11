"""Kinetica connector using the gpudb library."""

import os

import gpudb


def connect() -> gpudb.GPUdb:
    """Connect to Kinetica and return the GPUdb client.

    Environment Variables:
        KINETICA_HOST: Kinetica host (default: localhost)
        KINETICA_PORT: Kinetica port (default: 9191)
        KINETICA_USERNAME: Authentication username
        KINETICA_PASSWORD: Authentication password
    """
    host = os.environ.get("KINETICA_HOST", "localhost")
    port = int(os.environ.get("KINETICA_PORT", "9191"))
    username = os.environ.get("KINETICA_USERNAME", "<username>")
    password = os.environ.get("KINETICA_PASSWORD", "<password>")

    options = gpudb.GPUdb.Options()
    options.username = username
    options.password = password

    db = gpudb.GPUdb(host=f"http://{host}:{port}", options=options)
    return db


if __name__ == "__main__":
    try:
        db = connect()
        response = db.show_system_properties()
        print(f"Kinetica connected. Version: {response['property_map']['version.gpudb_core_version']}")
    except Exception as e:
        print(f"Failed to connect to Kinetica: {e}")
