FROM python:3
ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install xmlsec1

ADD . /code/
