from connectors.kafka_conector import KafkaConector
import os

class Producer:
    def __init__(self):
        self.conector = KafkaConector()
    def produce(self, message):
        producer = self.conector.producer
        producer.send(topic=os.getenv('KAFKA_TOPIC'), value=message)