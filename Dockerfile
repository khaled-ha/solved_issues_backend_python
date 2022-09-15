FROM python:3.9-slim-bullseye AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


# install python dependencies
RUN pip install --upgrade pip

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

FROM python:3.9-slim-bullseye

RUN mkdir /app
WORKDIR /app

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


# install python dependencies
RUN pip install --upgrade pip

COPY --from=builder /opt/venv /opt/venv
ENV  PATH="/opt/venv/bin:$PATH" 

COPY ./app /app