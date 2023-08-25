FROM python:3.11

WORKDIR /backend

COPY requirements.txt ./

RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean

RUN pip install -r requirements.txt && \
    rm -rf /root/.cache/pip

COPY . .
