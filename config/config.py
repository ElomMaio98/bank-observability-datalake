import os
from dataclasses import dataclass

@dataclass
class KafkaConfig:
    #configurações de conexão para o kafka
    brokers: str
    topic: str
    group_id: str
    worker_thread: int
    queue_maxsize: int

    @classmethod
    def from_env(cls):
        return cls(
            brokers = os.getenv("KAFKA_BROKERS"),
            topic = os.getenv("KAFKA_TOPIC"),
            group_id = os.getenv("KAFKA_GROUP_ID"),
            worker_thread = int(os.getenv("KAFKA_PRODUCER_WORKERS","4")),
            queue_maxsize = int(os.getenv("KAFKA_PRODUCER_QUEUE_MAXSIZE","5000"))
        )
    
@dataclass
class PostgresConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
    connection_timeout: int

    @classmethod
    def from_env(cls):
        return cls(
            host = os.getenv("POSTGRES_HOST"),
            port = int(os.getenv("POSTGRES_HOST")),
            database = os.getenv("POSTGRES_DB"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD"),
            connection_timeout = int(os.getenv("POSTGRES_CONNECTION_TIMEOUT"))
        )

