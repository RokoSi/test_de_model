import json
from confluent_kafka import Producer


def get_msg_json(user_json: list):

    producer = Producer({'bootstrap.servers': 'harmless-llama-10955-eu2-kafka.upstash.io:9092',
                         'sasl.mechanism': 'SCRAM-SHA-256',
                         'security.protocol': 'SASL_SSL',
                         'sasl.username': 'aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
                         'sasl.password': 'YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm'
                         })
    data_json = json.dumps(user_json)

    producer.produce('test_msg', value=data_json)
    producer.flush()
    print("Message sent successfully")
