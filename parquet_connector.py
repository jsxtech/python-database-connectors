import pyarrow.parquet as pq

def connect():
    table = pq.read_table("<filename>.parquet")
    return table

if __name__ == "__main__":
    table = connect()
    print(f"Parquet file loaded. Schema: {table.schema}")
