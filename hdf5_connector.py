"""HDF5 file reader using the h5py library.

Note: This is a file format reader, not a database connection.
It opens HDF5 (Hierarchical Data Format) files for reading and writing.
"""

import os

import h5py


def connect() -> h5py.File:
    """Open an HDF5 file and return the file handle.

    Note: This is a file reader, not a database connection.

    Environment Variables:
        HDF5_FILE: Path to the HDF5 file
        HDF5_MODE: File open mode (default: a for read/write/create)
    """
    filepath = os.environ.get('HDF5_FILE', '<filename>.h5')
    mode = os.environ.get('HDF5_MODE', 'a')

    file = h5py.File(filepath, mode)
    return file


if __name__ == "__main__":
    try:
        file = connect()
        print(f"HDF5 connected. Keys: {list(file.keys())}")
        file.close()
    except Exception as e:
        print(f"Failed to read HDF5 file: {e}")
