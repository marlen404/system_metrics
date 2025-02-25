from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.models.metrics_model import SystemMetrics
from app.queues.redis_queue import add_to_redis_queue
from app.queues.rabbitmq_queue import send_to_rabbitmq

async def queue_metric(metrics: dict):
    add_to_redis_queue(metrics)
    send_to_rabbitmq(metrics)
    return {"message": "Metric queued for processing"}

async def get_metrics_list(db: AsyncSession):
    result = await db.execute(select(SystemMetrics.id, SystemMetrics.service_name))
    return result.fetchall()

async def get_metric_by_id(id: int, db: AsyncSession):
    result = await db.execute(select(SystemMetrics).where(SystemMetrics.id == id))
    metric = result.scalar()
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric

async def delete_metric(id: int, db: AsyncSession):
    result = await db.execute(select(SystemMetrics).where(SystemMetrics.id == id))
    metric = result.scalar()
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")

    await db.delete(metric)
    await db.commit()
    return {"message": "Metric deleted"}