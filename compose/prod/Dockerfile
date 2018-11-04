FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r /code/requirements/base.txt

COPY ./compose/prod/start.sh /start.sh

RUN chmod +x /start.sh