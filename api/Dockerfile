# Use lightweight Python image
FROM python:3.11.9-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY api/ ./api
COPY services/ ./services
COPY models ./models
COPY api/requirements.txt .

RUN pip install --upgrade pip \
 && pip install \
    --default-timeout=300 \
    --retries 15 \
    -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]