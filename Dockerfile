# container to build tdlib for linux. example usage:
# docker buildx build . \
#  --target tdlib \
#  --platform linux/arm64 \
# --build-arg TDLIB_TAG=aiotdlib_0.19.0 \
# -o ./tdlib/
ARG PYTHONVERSION=3.9

FROM docker.io/library/debian:stable AS builder-tdlib

ARG TDLIB_TAG
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y git g++ cmake zlib1g-dev gperf libssl-dev
RUN git clone https://github.com/pylakey/td --depth 1 --branch $TDLIB_TAG
RUN mkdir td/build
WORKDIR td/build
RUN cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/tmp/tdlib/ -DTD_ENABLE_LTO=ON ..
RUN CMAKE_BUILD_PARALLEL_LEVEL=$(grep -c processor /proc/cpuinfo) cmake --build . --target install
RUN ls -la /tmp/tdlib/lib

FROM scratch AS tdlib

ARG TARGETARCH
COPY --from=builder-tdlib /tmp/tdlib/lib/libtdjson.so /libtdjson_linux_$TARGETARCH.so

# container to build wheels
# docker buildx build . --target wheel --build-arg PYTHONVERSION=3.10 --platform linux/arm64  -o ./dist/

FROM docker.io/library/python:$PYTHONVERSION-slim AS builder-wheel

RUN apt-get update -y && apt-get install -y --no-install-recommends curl

RUN python3 -m pip install wheel
RUN curl -fL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY README.md /aiotdlib/
COPY LICENSE /aiotdlib/
COPY poetry.lock /aiotdlib/
COPY pyproject.toml /aiotdlib/
COPY ./aiotdlib /aiotdlib/aiotdlib
COPY ./aiotdlib_generator /aiotdlib/aiotdlib_generator
COPY ./tdlib /aiotdlib/tdlib
COPY ./build.py /aiotdlib/build.py

WORKDIR /aiotdlib/

RUN poetry build

FROM scratch as wheel
COPY --from=builder-wheel ./aiotdlib/dist/* /
