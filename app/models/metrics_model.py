from sqlalchemy import Column, Integer, Float, String
from app.config.database import Base

class SystemMetrics(Base):
    __tablename__ = "system_metrics"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cpu_usage = Column(Float, nullable=False)
    ram_usage = Column(Float, nullable=False)
    network_traffic = Column(Float, nullable=False)
    timestamp = Column(String, nullable=False)
    service_name = Column(String, nullable=False)