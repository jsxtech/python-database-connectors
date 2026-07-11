"""RabbitMQ connector using the pika library."""

import os
from typing import Tuple

import pika


def connect() -> Tuple[pika.BlockingConnection, pika.adapters.blocking_connection.BlockingChannel]:
    """Connect to RabbitMQ and return the connection and channel.

    Environment Variables:
        RABBITMQ_HOST: RabbitMQ host (default: localhost)
        RABBITMQ_PORT: RabbitMQ port (default: 5672)
        RABBITMQ_USERNAME: Authentication username
        RABBITMQ_PASSWORD: Authentication password
    """
    host = os.environ.get('RABBITMQ_HOST', 'localhost')
    port = int(os.environ.get('RABBITMQ_PORT', '5672'))
    username = os.environ.get('RABBITMQ_USERNAME', '<username>')
    password = os.environ.get('RABBITMQ_PASSWORD', '<password>')

    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, port=port, credentials=credentials)
    )
    channel = connection.channel()
    return connection, channel


if __name__ == "__main__":
    try:
        connection, channel = connect()
        print(f"RabbitMQ connected. Channel: {channel}")
        connection.close()
    except Exception as e:
        print(f"Failed to connect to RabbitMQ: {e}")
