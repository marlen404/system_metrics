""" Settings """
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
RABITMQ_URL = os.getenv("RABITMQ_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set")

if not REDIS_URL:
    raise ValueError("REDIS_URL not set")

if not RABITMQ_URL:
    raise ValueError("RABITMQ_URL not set")
