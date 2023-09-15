FROM python:3.11

WORKDIR /backend


RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean

COPY requirements.txt ./

RUN pip install -r requirements.txt && \
    rm -rf /root/.cache/pip

COPY . .
