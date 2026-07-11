"""Parquet file reader using PyArrow.

Note: This is a file format reader, not a database connection.
It reads Apache Parquet columnar data files from the local filesystem.
"""

import os

import pyarrow.parquet as pq
import pyarrow


def connect() -> pyarrow.Table:
    """Read a Parquet file and return a PyArrow Table.

    Note: This is a file reader, not a database connection.

    Environment Variables:
        PARQUET_FILE: Path to the Parquet file to read
    """
    filepath = os.environ.get('PARQUET_FILE', '<filename>.parquet')

    table = pq.read_table(filepath)
    return table


if __name__ == "__main__":
    try:
        table = connect()
        print(f"Parquet file loaded. Schema: {table.schema}")
    except Exception as e:
        print(f"Failed to read Parquet file: {e}")
