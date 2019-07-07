FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY docker_requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install -r docker_requirements.txt
COPY . /code/
