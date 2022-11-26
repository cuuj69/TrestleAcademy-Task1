FROM python:3.10.4

WORKDIR /fastapi-app

COPY requirements.txt .

CMD ["python", "./main.py"]