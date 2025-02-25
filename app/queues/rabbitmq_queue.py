import pika
import json

def send_to_rabbitmq(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue="metrics_queue")
    channel.basic_publish(exchange='', routing_key="metrics_queue", body=json.dumps(data))
    connection.close()                                                               
                                                                   