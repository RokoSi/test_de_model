import json
import logging

from confluent_kafka import Producer

from settings import settings

log = logging.getLogger(__name__)


def get_msg_json(user_json: list):
    """
    Отправляет сообщения через kafka
    :param user_json: полученный пользователь
    """

    producer = Producer(
        {
            "bootstrap.servers": "harmless-llama-10955-eu2-kafka.upstash.io:9092",
            "sasl.mechanism": "SCRAM-SHA-256",
            "security.protocol": "SASL_SSL",
            "sasl.username": settings.user_kafka,
            "sasl.password": settings.password_kafka,
        }
    )
    data_json = json.dumps(user_json)

    producer.produce(settings.topic, value=data_json)
    producer.flush()

    print("Message sent successfully")
