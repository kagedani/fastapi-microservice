FROM python:3.8-slim

WORKDIR /movie-service
ENV env=test

COPY ./requirements.txt /movie-service/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /movie-service/requirements.txt \
    && rm -rf /root/.cache/pip

COPY app/* .