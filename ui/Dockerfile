FROM python:3.11-slim

WORKDIR /app

COPY ui/requirements.txt .

RUN pip install --upgrade pip \
 && pip install \
    --default-timeout=300 \
    --retries 15 \
    -r requirements.txt

COPY ui/ .

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]