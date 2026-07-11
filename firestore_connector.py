"""Google Cloud Firestore connector using google-cloud-firestore."""

import os

from google.cloud import firestore


def connect() -> firestore.Client:
    """Connect to Google Cloud Firestore.

    Environment variables:
        FIRESTORE_PROJECT: GCP project ID
    """
    db = firestore.Client(project=os.environ.get('FIRESTORE_PROJECT', '<project-id>'))
    return db


if __name__ == "__main__":
    try:
        db = connect()
        collections = db.collections()
        print(f"Firestore connected. Collections: {[c.id for c in collections]}")
    except Exception as e:
        print(f"Error connecting to Firestore: {e}")
