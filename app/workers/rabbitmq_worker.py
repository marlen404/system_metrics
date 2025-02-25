import pika
import json
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.models.metrics_model import SystemMetrics

def callback(ch, method, properties, body):
    db = next(get_db())
    metric_data = json.loads(body)

    new_metric = SystemMetrics(**metric_data)
    db.add(new_metric)
    db.commit()

    ch.basic_ack(delivery_tag=method.delivery_tag)

def process_rabbitmq_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue="metrics_queue")
    channel.basic_consume(queue="metrics_queue", on_message_callback=callback)
    channel.start_consuming()