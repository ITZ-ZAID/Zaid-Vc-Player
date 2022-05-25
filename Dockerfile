FROM python:3.10-slim-buster
WORKDIR /app
RUN apt-get -y update
RUN apt-get -y install git gcc python3-dev
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "main.py"]
