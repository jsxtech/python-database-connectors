from surrealdb import Surreal

def connect():
    db = Surreal("ws://localhost:8000/rpc")
    db.signin({"user": "<username>", "pass": "<password>"})
    db.use("<namespace>", "<database>")
    return db

if __name__ == "__main__":
    db = connect()
    result = db.query("INFO FOR DB")
    print(f"SurrealDB connected. Info: {result}")
    db.close()
