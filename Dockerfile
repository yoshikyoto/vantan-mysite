FROM python:3.9-slim-buster

WORKDIR /code

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code
# CMD python manage.py runserver 0:8000
CMD gunicorn -w 100 -b 0.0.0.0:8000 mysite.wsgi:application
