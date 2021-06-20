FROM python:3.9-slim-buster

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code
CMD python manage.py runserver 0:8000
