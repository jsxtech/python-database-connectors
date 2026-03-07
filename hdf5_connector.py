import h5py

def connect():
    file = h5py.File("<filename>.h5", "a")
    return file

if __name__ == "__main__":
    file = connect()
    print(f"HDF5 connected. Keys: {list(file.keys())}")
    file.close()
