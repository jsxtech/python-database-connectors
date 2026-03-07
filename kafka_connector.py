from kafka import KafkaProducer, KafkaConsumer

def connect():
    return connect_producer()

def connect_producer():
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"]
    )
    return producer

def connect_consumer():
    consumer = KafkaConsumer(
        "<topic>",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest"
    )
    return consumer

if __name__ == "__main__":
    producer = connect_producer()
    print(f"Kafka producer connected. Metrics: {producer.metrics()}")
    producer.close()
