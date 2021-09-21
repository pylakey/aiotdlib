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
cp -L td/tdlib/lib/libtdjson.dylib "aiotdlib/tdlib/libtdjson_darwin_$(uname -m).dylib"
