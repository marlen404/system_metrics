Sytem Metrics API

Setup and Installation
1. Clone Repo: git clone https://github.com/marlen404/system_metrics.git
cd system_metrics
2. Set up environment variables
Create .env file
3. Run (Docker)
docker-compose up --build

API Endpoints:

POST /metrics -queue new metric for background processing

GET /metrics -return a list of IDs of all stored system metrics in the database

GET /metrics/{id} -return a single system metric by ID

DELETE /metrics/{id} -delete a system metric by ID from the
database, If the ID does not exist, return a 404 error