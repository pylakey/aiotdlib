FROM python:3.9-slim-buster

LABEL maintainer="Pylakey <pylakey@protonmail.com>"
ENV AIOTDLIB_VERSION="0.8.3"

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libssl-dev \
    libc++-dev \
    libc++abi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip setuptools wheel
RUN pip install --no-cache-dir "aiotdlib==$AIOTDLIB_VERSION"
