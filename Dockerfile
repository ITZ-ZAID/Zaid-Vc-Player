FROM nikolaik/python-nodejs:python3.10-nodejs17
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN pip3 install -U -r requirements.txt
COPY start /start
CMD ["/bin/bash", "/start"]
