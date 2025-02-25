import redis
import json

redis_client = redis.Redis(host='redis', port=6379, decode_response=True)

def add_to_redis_queue(data):
    redis_client.rpush("metrics_queue", json.dumps(data))
