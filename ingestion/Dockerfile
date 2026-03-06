FROM python:3.11.9-slim

# Prevent Python from writing .pyc files & enable stdout flushing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

COPY ingestion/ ./ingestion
COPY services/ ./services
COPY ingestion/requirements.txt .


RUN pip install --upgrade pip \
 && pip install \
    --default-timeout=300 \
    --retries 15 \
    -r requirements.txt

# Expose Flask default port
EXPOSE 5000

# Production server (recommended)
CMD ["python", "-m", "ingestion.app"]