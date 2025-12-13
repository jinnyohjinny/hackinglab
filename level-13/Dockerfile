FROM python:3.11-alpine

RUN apk add --no-cache iputils

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/
COPY static/ static/

EXPOSE 80

CMD ["python", "app.py"]
