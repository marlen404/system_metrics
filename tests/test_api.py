import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config.database import get_db, Base, engine, SessionLocal

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_metric():
    response = client.post("/metrics/", json={
        "cpu_usage": 45.7,
        "ram_usage": 62.1,
        "network_traffic": 215.7,
        "timestamp": "20250224T143600Z",
        "service_name": "web-server"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Metric queued successfully"}

def test_get_metrics():
    response = client.get("/metrics/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_metric_not_found():
    response = client.get("/metrics/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Metric not found"}

def test_delete_metric_not_found():
    response = client.delete("/metrics/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Metric not found"}
