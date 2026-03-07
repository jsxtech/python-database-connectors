import pinecone

def connect():
    pinecone.init(api_key="<api-key>", environment="<environment>")
    return pinecone

if __name__ == "__main__":
    pc = connect()
    indexes = pc.list_indexes()
    print(f"Pinecone connected. Indexes: {indexes}")
