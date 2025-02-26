
ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


# Copy the source code into the container.
COPY . /app

# Expose port 8000
EXPOSE 8000

# Run the application.
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
