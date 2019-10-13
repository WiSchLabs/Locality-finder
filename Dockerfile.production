FROM python:3

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/WiSchLabs/Locality-finder" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Locality Finder" \
      org.label-schema.vendor="WischLabs" \
      org.label-schema.schema-version="1.0"

CMD ["gunicorn", "locality_finder.wsgi", "--bind", ":8000"]

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev python3-gdal && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY requirements.production.txt /code/
RUN pip install -r requirements.production.txt

COPY . /code/
