FROM python:3.11-slim
WORKDIR /app/src
ENV PYTHONPATH=/app/src:/app
COPY . /app
RUN pip install -r /app/requirements.txt