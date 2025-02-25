from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.services.metrics_service import (
    queue_metric, get_metrics_list, get_metric_by_id, delete_metric
)
from app.models.metrics_model import SystemMetrics

router = APIRouter()

@router.post("/")
async def post_metrics(metrics: SystemMetrics, db: AsyncSession = Depends(get_db)):
    return await queue_metric(metrics.dict())

@router.get("/")
async def get_metrics_list(db: AsyncSession = Depends(get_db)):
    return await get_metrics_list(db)

@router.get("/{id}")
async def get_metric(id: int, db: AsyncSession = Depends(get_db)):
    return await get_metric_by_id(id, db)

@router.delete("/{id}")
async def delete_metric(id: int, db: AsyncSession = Depends(get_db)):
    return await delete_metric(id, db)