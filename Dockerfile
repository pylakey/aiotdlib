FROM python:3.9-slim

LABEL maintainer="Pylakey <pylakey@protonmail.com>"

ENV AIOTDLIB_VERSION="0.7.1"

RUN pip install --no-cache-dir "aiotdlib==$AIOTDLIB_VERSION"
