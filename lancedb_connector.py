import lancedb

def connect():
    db = lancedb.connect("<path-to-db>")
    return db

if __name__ == "__main__":
    db = connect()
    tables = db.table_names()
    print(f"LanceDB connected. Tables: {tables}")
