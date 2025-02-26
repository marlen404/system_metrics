import pytest
import json
from app.queues.redis_queue import enqueue_metric, dequeue_metric
from app.queues.rabbitmq_queue import enqueue_metric as rabbit_enqueue, dequeue_metric as rabbit_dequeue

metric_data = {
    "cpu_usage": 42.7,
    "ram_usage": 61.4,
    "network_traffic": 214.3,
    "timestamp": "2025",
    "service_name": "web-server"
}

def test_redis_queue():
    enqueue_metric(metric_data)
    retrieved_data = dequeue_metric()
    assert retrieved_data == metric_data

def test_rabbitmq_queue():
    rabbit_enqueue(metric_data)

    def callback(ch, method, properties, body):
        retrieved_data = json.loads(body)
        assert retrieved_data == metric_data

    rabbit_dequeue(None, None, None, json.dumps(metric_data).encode('utf-8'))