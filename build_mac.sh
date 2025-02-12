#!/usr/bin/env sh
set -e
rm -rf td/
git clone https://github.com/pylakey/td.git
cd td
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release \
      -DOPENSSL_ROOT_DIR=/opt/homebrew/opt/openssl/ \
      -DCMAKE_INSTALL_PREFIX:PATH=../tdlib \
      -DTD_ENABLE_LTO=ON \
      ..
cmake --build . --target install
cd ..
cd ..
ls -l td/tdlib
