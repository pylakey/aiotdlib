#!/usr/bin/env sh
set -e
rm -rf td/
git clone https://github.com/pylakey/td
cd td
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release \
      -DOPENSSL_ROOT_DIR=/opt/homebrew/opt/openssl/ \
      -DCMAKE_INSTALL_PREFIX:PATH=../tdlib \
      -DTD_ENABLE_LTO=ON \
      ..
cmake --build . --target install
cd ../..
BINARY_DIR="../aiotdlib/tdlib/darwin/$(uname -m)"
mkdir -p "$BINARY_DIR"
mv td/tdlib/lib/libtdjson.1.7.6.dylib "$BINARY_DIR/libtdjson.dylib"
rm -rf td