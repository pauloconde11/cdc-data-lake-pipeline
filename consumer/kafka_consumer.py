from kafka import KafkaConsumer
import json
from config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    KAFKA_GROUP_ID,
    KAFKA_AUTO_OFFSET_RESET,
)


def deserialize_message(data):
    if data is None:
        return None

    return json.loads(data.decode("utf-8"))


def create_kafka_consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=deserialize_message,
        auto_offset_reset=KAFKA_AUTO_OFFSET_RESET,
        group_id=KAFKA_GROUP_ID,
        enable_auto_commit=True,
    )
    return consumer