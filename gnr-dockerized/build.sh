#!/bin/bash
docker build -t gnr \
  --build-arg dkuser=$(id -un) \
  --build-arg dkuid=$(id -u) \
  --build-arg dkgroup=$(id -gn) \
  --build-arg dkgid=$(id -g) \
  .
