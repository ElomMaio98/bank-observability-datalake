from connectors.kafka_conector import KafkaConector
from kafka import KafkaProducer



class Producer:
    def __init__(self):
        conector = KafkaConector()
        conector.producer
        self.conector = conector
