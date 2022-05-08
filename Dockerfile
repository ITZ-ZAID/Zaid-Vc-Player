# syntax=docker/dockerfile:1

FROM nikolaik/python-nodejs:python3.10-nodejs17FROM nikolaik/python-nodejs:python3.10-nodejs17

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN apt-get -y install git gcc python3-dev
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY start /start
CMD ["/bin/bash", "/start"]
