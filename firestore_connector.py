from google.cloud import firestore

def connect():
    db = firestore.Client(project="<project-id>")
    return db

if __name__ == "__main__":
    db = connect()
    collections = db.collections()
    print(f"Firestore connected. Collections: {[c.id for c in collections]}")
