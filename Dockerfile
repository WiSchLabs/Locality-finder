FROM python:3

EXPOSE 8080

RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev python3-gdal && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
