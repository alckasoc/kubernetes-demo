FROM python:3.9-slim

COPY service_a.py /app/
WORKDIR /app
RUN pip install --no-cache-dir flask gunicorn

CMD ["gunicorn", "-b", "0.0.0.0:8000", "service_a:app"]
