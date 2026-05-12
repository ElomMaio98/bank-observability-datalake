from connectors.kafka_conector import KafkaConector
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Consumer():
    def __init__(self):
        self.consumer = KafkaConector()
    def consume(self):
        consumer = self.consumer.consumer
        consumer.subscribe(topics=[os.getenv("KAFKA_TOPIC")])
        while True:
            try:
                messages = consumer.poll(timeout_ms=1000)
                logger.info('Mensagem consumida')
            except TimeoutError as t:
                logger.error(f'Tempo expirado: {t}')