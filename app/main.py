from fastapi import FastAPI
from app.routes import metrics_routes
from app.config.database import create_tables

app = FastAPI(title="Metrics API")

app.include_router(metrics_routes.router)

@app.on_event("startup")
async def startup():
    create_tables()

@app.get("/")
def read_root():
    return {"message": "Metrics API is running"}