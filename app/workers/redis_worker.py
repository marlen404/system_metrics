from app.queues.redis_queue import dequeue_metric
from app.config.database import SessionLocal
from app.models.metrics_model import Metric

def process_metrics():
    db = SessionLocal()
    while True:
        metric_data = dequeue_metric()
        metric = Metric(**metric_data)
        db.add(metric)
        db.commit()