FROM python:latest

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./web /automation/web
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install