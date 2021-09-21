FROM python:3.9-slim-bullseye

LABEL maintainer="Pylakey <pylakey@protonmail.com>"

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libssl-dev \
    libc++-dev \
    libc++abi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip setuptools wheel
RUN pip install --no-cache-dir aiotdlib
