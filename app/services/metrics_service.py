from sqlalchemy.orm import Session
from app.models.metrics_model import Metric

def create_metric(db: Session, metric_data: dict):
    """
    Inserts a new metric into the database.
    """
    metric = Metric(**metric_data)
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric

def get_all_metrics(db: Session):
    """
    Fetches all stored metrics.
    """
    return db.query(Metric).all()

def get_metric_by_id(db: Session, metric_id: int):
    """
    Retrieves a specific metric by ID.
    """
    return db.query(Metric).filter(Metric.id == metric_id).first()

def delete_metric_by_id(db: Session, metric_id: int):
    """
    Deletes a specific metric by ID.
    """
    metric = db.query(Metric).filter(Metric.id == metric_id).first()
    if metric:
        db.delete(metric)
        db.commit()
        return True
    return False