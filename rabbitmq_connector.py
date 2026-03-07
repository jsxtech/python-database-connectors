import pika

def connect():
    credentials = pika.PlainCredentials("<username>", "<password>")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", credentials=credentials)
    )
    channel = connection.channel()
    return connection, channel

if __name__ == "__main__":
    connection, channel = connect()
    print(f"RabbitMQ connected. Channel: {channel}")
    connection.close()
