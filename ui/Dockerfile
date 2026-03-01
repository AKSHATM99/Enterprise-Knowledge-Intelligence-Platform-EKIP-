# Use official lightweight Python image
FROM python:3.11.9-slim

# Prevent Python from writing pyc files & enable stdout flushing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# # Install system dependencies (if needed)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install Python dependencies (no pip self-upgrade)
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]