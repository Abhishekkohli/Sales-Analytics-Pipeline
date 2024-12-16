from kafka import KafkaConsumer
import psycopg2
import json

# Kafka Configuration
KAFKA_TOPIC = 'sales_events'
KAFKA_BROKER = 'localhost:9092'

# PostgreSQL Configuration
DB_CONFIG = {
    'dbname': 'retail_analytics',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

# Connect to PostgreSQL
def connect_to_postgres():
    return psycopg2.connect(**DB_CONFIG)

# Process and store sales events
def consume_sales_events():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    conn = connect_to_postgres()
    cursor = conn.cursor()

    for message in consumer:
        event = message.value
        cursor.execute("""
            INSERT INTO fact_sales (order_date, customer_id, product_id, quantity, total_price)
            VALUES (%s, %s, %s, %s, %s)
        """, (event['order_date'], event['customer_id'], event['product_id'], event['quantity'], event['quantity'] * event['unit_price']))
        conn.commit()
        print(f"Inserted: {event}")

if __name__ == "__main__":
    consume_sales_events()
