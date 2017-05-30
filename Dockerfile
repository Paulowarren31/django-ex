FROM ubuntu:16.04
ENV PYTHONUNBUFFERED 1

RUN mkdir /code


WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update && apt-get -y install xmlsec1

RUN pip install --upgrade pip && \
      pip install -r requirements.txt

EXPOSE 8000

ADD . /code/

CMD python manage.py migrate; python manage.py runserver 0.0.0.0:8080
