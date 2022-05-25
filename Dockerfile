FROM node:16-buster-slim
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
