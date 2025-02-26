from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.metrics_service import (
    create_metric, get_all_metrics, get_metric_by_id, delete_metric_by_id
)
from app.queues.redis_queue import enqueue_metric

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.post("/")
def create_metric_endpoint(metric: dict, db: Session = Depends(get_db)):
    """
    Queues a new metric and returns a success message.
    """
    enqueue_metric(metric)
    return {"message": "Metric queued successfully"}

@router.get("/")
def get_metrics_endpoint(db: Session = Depends(get_db)):
    """
    Returns a list of stored metrics.
    """
    metrics = get_all_metrics(db)
    return [{"id": m.id, "service_name": m.service_name} for m in metrics]

@router.get("/{id}")
def get_metric_endpoint(id: int, db: Session = Depends(get_db)):
    """
    Returns details of a specific metric.
    """
    metric = get_metric_by_id(db, id)
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric

@router.delete("/{id}")
def delete_metric_endpoint(id: int, db: Session = Depends(get_db)):
    """
    Deletes a metric by ID.
    """
    success = delete_metric_by_id(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Metric not found")
    return {"message": "Metric deleted successfully"}