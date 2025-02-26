import json
import pika
from app.config.settings import RABBITMQ_URL
from app.config.database import SessionLocal
from app.services.metrics_service import create_metric

params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="metrics_queue", durable=True)

def callback(ch, method, properties, body):
    db = SessionLocal()
    try:
        metric_data = json.loads(body)
        create_metric(db, metric_data)
        db.commit()
    except Exception as e:
        print("Error processing metric:", e)
    finally:
        db.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue="metrics_queue", on_message_callback=callback)
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()