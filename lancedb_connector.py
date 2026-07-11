"""LanceDB vector database connector using lancedb."""

import os

import lancedb


def connect() -> lancedb.DBConnection:
    """Connect to LanceDB.

    Environment variables:
        LANCEDB_PATH: Path to LanceDB storage directory (default: <path-to-db>)
    """
    path = os.environ.get('LANCEDB_PATH', '<path-to-db>')
    db = lancedb.connect(path)
    return db


if __name__ == "__main__":
    try:
        db = connect()
        tables = db.table_names()
        print(f"LanceDB connected. Tables: {tables}")
    except Exception as e:
        print(f"Failed to connect to LanceDB: {e}")
