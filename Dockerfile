FROM python:3

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 8080

CMD ["python", "app.py"]
