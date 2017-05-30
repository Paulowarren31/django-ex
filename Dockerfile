FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

RUN apt-get update

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install xmlsec1

EXPOSE 8000

ADD . /code/

CMD python2 manage.py migrate; python2 manage.py runserver 0.0.0.0:8080
