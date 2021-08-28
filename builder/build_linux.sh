#!/usr/bin/env sh
set -e
earthly --platform="linux/arm64" +build
earthly --platform="linux/amd64" +build