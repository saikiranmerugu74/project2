FROM python:3.9-slim

# Install dockerize using curl
RUN apt-get update && apt-get install -y curl \
    && curl -L https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz | tar -C /usr/local/bin -xz \
    && apt-get remove -y curl && apt-get autoremove -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python", "app.py"]

CMD ["dockerize", "-wait", "tcp://db:3306", "-timeout", "60s", "python", "app.py"]