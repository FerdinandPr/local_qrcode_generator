FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY qr.py .

# Ausgabeverzeichnis (wird zur Laufzeit per Volume-Mount überdeckt).
# Schreibbar für beliebige UID (z. B. OpenShift, --user).
RUN mkdir /output && chmod 777 /output

# Nicht-root-Default; per --user überschreibbar
USER 1001

ENTRYPOINT ["python", "/app/qr.py"]
