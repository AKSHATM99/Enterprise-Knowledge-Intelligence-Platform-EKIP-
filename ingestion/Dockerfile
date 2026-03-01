FROM python:3.11.9-slim

# Prevent Python from writing .pyc files & enable stdout flushing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# # Install system dependencies (only if required)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Copy dependency file first (for Docker caching)
COPY requirements.txt .

# Install Python dependencies (no pip self-upgrade)
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Flask default port
EXPOSE 5000

# Production server (recommended)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]