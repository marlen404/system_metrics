import redis
import json
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.models.metrics_model import SystemMetrics

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

async def process_redis_queue(db: AsyncSession):
    while True:
        _, data = redis_client.blpop("metrics_queue")
        metric_data = json.loads(data)

        new_metric = SystemMetrics(**metric_data)
        db.add(new_metric)
        await db.commit()