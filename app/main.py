from fastapi import FastAPI
from app.routes import metrics_routes
from app.config.database import create_tables

app = FastAPI(title="Metrics API")

app.include_router(metrics_routes)