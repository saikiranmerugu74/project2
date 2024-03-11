FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python", "app.py"]

CMD ["dockerize", "-wait", "tcp://db:3306", "-timeout", "60s", "python", "app.py"]