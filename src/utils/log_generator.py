from faker import Faker 
from datetime import datetime
import random

fake = Faker()

def generate_logs():
    return{
        "date":datetime.now(),
        "level": random.choice(["ERROR",'WARN','INFO']),
        "message": fake.paragraph(),
        "service":random.choice(["auth-service","payment-service","db-worker"])
        }
