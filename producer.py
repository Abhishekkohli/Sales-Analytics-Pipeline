from kafka import KafkaProducer
import json
import time
import pandas as pd

# Kafka Configuration
KAFKA_TOPIC = 'sales_events'
KAFKA_BROKER = 'localhost:9092'

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate real-time sales events
def publish_sales_events(file_path):
    sales_data = pd.read_csv(file_path)
    for _, row in sales_data.iterrows():
        event = row.to_dict()
        producer.send(KAFKA_TOPIC, value=event)
        print(f"Published: {event}")
        time.sleep(1)  # Simulate real-time streaming

if __name__ == "__main__":
    publish_sales_events('../data/sales.csv')
