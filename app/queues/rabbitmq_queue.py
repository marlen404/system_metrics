import pika
import json
from app.config.settings import RABBITMQ_URL

params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="metrics_queue")

def enqueue_metric(metric_data):
    channel.basic_publish(exchange="", routing_key="metrics_queue", body=json.dumps(metric_data))

def dequeue_metric(ch, method, properties, body):
    return json.loads(body)