build-all-platforms:
    BUILD --platform=linux/arm64 +build

builder:
    FROM debian:bullseye

    ENV DEBIAN_FRONTEND noninteractive
    ENV DEBCONF_NONINTERACTIVE_SEEN true

    RUN apt-get update && apt-get -y install \
        git \
        make \
        zlib1g-dev \
        libssl-dev \
        gperf \
        cmake \
        clang \
        libc++-dev \
        libc++abi-dev \
        && rm -rf /var/lib/apt/lists/*


build:
    FROM +builder
    GIT CLONE https://github.com/pylakey/td /code
    WORKDIR /build

    RUN CXXFLAGS="-stdlib=libc++" \
        CC=/usr/bin/clang \
        CXX=/usr/bin/clang++ \
        cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX:PATH=/tdlib \
        -S /code \
        -B /build

    RUN cmake --build /build --target install

    ARG TARGETARCH
    SAVE ARTIFACT /tdlib/lib/libtdjson.so AS LOCAL aiotdlib/tdlib/libtdjson_linux_${TARGETARCH}.so
