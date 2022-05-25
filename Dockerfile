FROM node:16-buster-slim
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN apt-get -y install git gcc python3-dev
COPY . /app/
WORKDIR /app/
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
