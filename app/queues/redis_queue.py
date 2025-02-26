import redis
import json
from app.config.settings import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def enqueue_metric(metric_data):
    redis_client.rpush("metrics_queue", json.dumps(metric_data))

def dequeue_metric():
    _, data = redis_client.blpop("metrics_queue")
    return json.loads(data)