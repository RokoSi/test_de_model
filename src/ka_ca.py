
from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField

from src.json_parsing.model.users import Users

from kafka import KafkaProducer


def get_msg():
    producer = KafkaProducer(
        bootstrap_servers='harmless-llama-10955-eu2-kafka.upstash.io:9092',
        sasl_mechanism='SCRAM-SHA-256',
        security_protocol='SASL_SSL',
        sasl_plain_username='aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
        sasl_plain_password='YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm'
    )

    try:
        producer.send('test_msg', b'Hello from python')
        producer.flush()
        print("Message produced without Avro schema!")
    except Exception as e:
        print(f"Error producing message: {e}")
    finally:
        producer.close()


def get_msg_json(user0: Users, valid: bool):
    schema = """
    {
      "type": "record",
      "name": "User",
      "namespace": "com.upstash",
      "fields": [
        {"name": "gender", "type": "string"},
        {"name": "name", "type": {
          "type": "record",
          "name": "Name",
          "fields": [
            {"name": "title", "type": "string"},
            {"name": "first", "type": "string"},
            {"name": "last", "type": "string"}
          ]
        }},
        {"name": "location", "type": {
          "type": "record",
          "name": "Location",
          "fields": [
            {"name": "street", "type": {
              "type": "record",
              "name": "Street",
              "fields": [
                {"name": "name", "type": "string"},
                {"name": "number", "type": "int"}
              ]
            }},
            {"name": "city", "type": "string"},
            {"name": "state", "type": "string"},
            {"name": "country", "type": "string"},
            {"name": "postcode", "type": "string"},
            {"name": "coordinates", "type": {
              "type": "record",
              "name": "Coordinates",
              "fields": [
                {"name": "latitude", "type": "double"},
                {"name": "longitude", "type": "double"}
              ]
            }}
          ]
        }},
        {"name": "dob", "type": {
          "type": "record",
          "name": "Dob",
          "fields": [
            {"name": "age", "type": "int"}
          ]
        }},
        {"name": "nat", "type": "string"},
        {"name": "email", "type": "string"},
        {"name": "login", "type": {
          "type": "record",
          "name": "RegistrationData",
          "fields": [
            {"name": "username", "type": "string"},
            {"name": "password", "type": "string"},
            {"name": "md5", "type": "string"}
          ]
        }},
        {"name": "registered", "type": {
          "type": "record",
          "name": "Registered",
          "fields": [
            {"name": "date", "type": "string"},
            {"name": "age", "type": "int"}
          ]
        }},
        {"name": "phone", "type": "string"},
        {"name": "cell", "type": "string"},
        {"name": "picture", "type": {
          "type": "record",
          "name": "MediaData",
          "fields": [
            {"name": "large", "type": "string"},
            {"name": "medium", "type": "string"},
            {"name": "thumbnail", "type": "string"}
          ]
        }}
      ]
    }
    """
    user_dict = {
        "gender": user0.gender,
        "name": {
            "title": user0.name.title,
            "first": user0.name.first,
            "last": user0.name.last
        },
        "location": {
            "street": {
                "name": user0.location.street.name,
                "number": user0.location.street.number
            },
            "city": user0.location.city,
            "state": user0.location.state,
            "country": user0.location.country,
            "postcode": str(user0.location.postcode),
            "coordinates": {
                "latitude": user0.location.coordinates.latitude,
                "longitude": user0.location.coordinates.longitude
            }
        },
        "dob": {
            "age": user0.dob.age
        },
        "nat": user0.nat,
        "email": user0.email,
        "login": {
            "username": user0.login.username,
            "password": user0.login.password,
            "md5": user0.login.md5
        },
        "registered": {
            "date": user0.registered.date,
            "age": user0.registered.age
        },
        "phone": user0.phone,
        "cell": user0.cell,
        "picture": {
            "large": user0.picture.large,
            "medium": user0.picture.medium,
            "thumbnail": user0.picture.thumbnail
        },
        "valid": valid
    }


    schema_registry_client = SchemaRegistryClient({
        'url': "https://harmless-llama-10955-eu2-rest-kafka.upstash.io/schema-registry",
        'basic.auth.user.info': "aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU:YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm"
    })

    avro_serializer = AvroSerializer(schema_registry_client, schema)

    string_serializer = StringSerializer('utf_8')

    producer = Producer({'bootstrap.servers': 'harmless-llama-10955-eu2-kafka.upstash.io:9092',
                         'sasl.mechanism': 'SCRAM-SHA-256',
                         'security.protocol': 'SASL_SSL',
                         'sasl.username': 'aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
                         'sasl.password': 'YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm'
                         })

    producer.produce(topic="test_msg",
                     key=string_serializer("id"),
                     value=avro_serializer(user_dict, SerializationContext("test_msg", MessageField.VALUE)))

    producer.flush()
    print("Message sent successfully")
