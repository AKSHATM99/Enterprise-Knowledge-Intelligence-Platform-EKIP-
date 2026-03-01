# Use lightweight Python image
FROM python:3.11.9-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (uncomment if you add OS-level deps)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (Docker cache optimization)
# Root requirements (shared libs for RAG, etc.)
COPY requirements.txt ./requirements.txt
# API-specific requirements
COPY api/requirements.txt ./api-requirements.txt

# Install Python dependencies (no pip self-upgrade to avoid resolver issues)
RUN pip install --no-cache-dir -r requirements.txt -r api-requirements.txt

# Copy the entire project into the image so FastAPI
# can import shared packages like `services` and `models`
COPY . .

# Expose API port
EXPOSE 8000

# Start FastAPI with Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]