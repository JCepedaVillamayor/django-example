FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements/ /code/requirements/
RUN pip install -r requirements/local.txt
ADD . /code/