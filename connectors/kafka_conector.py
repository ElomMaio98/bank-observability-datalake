from kafka import KafkaProducer, KafkaConsumer
from config.config import KafkaConfig

class KafkaConector:
    def __init__(self):
        configs = KafkaConfig.from_env()
        consumer = KafkaConsumer(
            configs.topic,
            bootstrap_servers = configs.brokers,
            group_id = configs.group_id
        )
        self.consumer = consumer
        self.producer = KafkaProducer(bootstrap_servers = configs.brokers)