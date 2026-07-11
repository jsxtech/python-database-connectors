"""Apache Kafka connector using the kafka-python library."""

import os

from kafka import KafkaProducer, KafkaConsumer


def connect() -> KafkaProducer:
    """Connect to Kafka and return a producer (default entry point).

    Environment Variables:
        KAFKA_BOOTSTRAP_SERVERS: Comma-separated broker addresses (default: localhost:9092)
        KAFKA_TOPIC: Topic name for consumer connections
    """
    return connect_producer()


def connect_producer() -> KafkaProducer:
    """Create and return a Kafka producer.

    Environment Variables:
        KAFKA_BOOTSTRAP_SERVERS: Comma-separated broker addresses (default: localhost:9092)
    """
    servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

    producer = KafkaProducer(
        bootstrap_servers=servers.split(',')
    )
    return producer


def connect_consumer() -> KafkaConsumer:
    """Create and return a Kafka consumer.

    Environment Variables:
        KAFKA_BOOTSTRAP_SERVERS: Comma-separated broker addresses (default: localhost:9092)
        KAFKA_TOPIC: Topic to subscribe to
    """
    servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    topic = os.environ.get('KAFKA_TOPIC', '<topic>')

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=servers.split(','),
        auto_offset_reset="earliest"
    )
    return consumer


if __name__ == "__main__":
    try:
        producer = connect()
        print(f"Kafka producer connected. Metrics: {producer.metrics()}")
        producer.close()
    except Exception as e:
        print(f"Failed to connect to Kafka: {e}")
