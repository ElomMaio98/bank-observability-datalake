from producer import Producer
from utils.log_generator import generate_logs
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_to_kafka():
    producer = Producer()
    for i in range(0,int(os.getenv("BATCH_SIZE"))):
        try:
            producer.produce(generate_logs())
            logger.info("Mensagem Enviada"),
        except Exception as e:
            logger.warning(f"Erro ao enviar a mensagem: {e}")


if __name__ == "__main__":
    send_to_kafka()