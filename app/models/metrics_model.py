from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SystemMetrics(Base):
    __tablename__ = "system_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    cpu_usage = Column(Float, nullable=False)
    ram_usage = Column(Float, nullable=False)
    network_traffic = Column(Float, nullable=False)
    timestamp = Column(String, nullable=False)
    service_name = Column(String, nullable=False)