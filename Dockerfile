FROM python:3.9-slim-buster

LABEL maintainer="Pylakey <pylakey@protonmail.com>"
ENV AIOTDLIB_VERSION="0.8.0"

RUN pip install -U pip setuptools wheel
RUN pip install --no-cache-dir "aiotdlib==$AIOTDLIB_VERSION"

COPY ./docker_app /app
WORKDIR /app/
ENV PYTHONPATH=/app

ENTRYPOINT ["/docker-entrypoint.sh"]