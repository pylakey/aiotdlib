FROM python:3.9-slim-buster

LABEL maintainer="Pylakey <pylakey@protonmail.com>"
ENV AIOTDLIB_VERSION="0.8.1"

RUN pip install -U pip setuptools wheel
RUN pip install --no-cache-dir "aiotdlib==$AIOTDLIB_VERSION"
