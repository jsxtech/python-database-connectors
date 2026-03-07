import pyarrow.feather as feather

def connect():
    table = feather.read_table("<filename>.feather")
    return table

if __name__ == "__main__":
    table = connect()
    print(f"Feather file loaded. Schema: {table.schema}")
