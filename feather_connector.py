"""Feather file reader using PyArrow.

Note: This is a file format reader, not a database connection.
It reads Apache Arrow Feather (IPC) files from the local filesystem.
"""

import os

import pyarrow.feather as feather
import pyarrow


def connect() -> pyarrow.Table:
    """Read a Feather file and return a PyArrow Table.

    Note: This is a file reader, not a database connection.

    Environment Variables:
        FEATHER_FILE: Path to the Feather file to read
    """
    filepath = os.environ.get('FEATHER_FILE', '<filename>.feather')

    table = feather.read_table(filepath)
    return table


if __name__ == "__main__":
    try:
        table = connect()
        print(f"Feather file loaded. Schema: {table.schema}")
    except Exception as e:
        print(f"Failed to read Feather file: {e}")
