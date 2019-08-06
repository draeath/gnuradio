#!/bin/bash

runtime() {
  if hash docker 2>/dev/null; then
    docker "$@"
  elif hash podman 2>/dev/null; then
    podman "$@"
  else
    echo "You need docker or podman!" >&2
    exit 1
  fi
}

DATEVAL="$(date -Idate)"

runtime build -t "gnuradio:$DATEVAL" \
  --build-arg dkuser="$(id -un)" \
  --build-arg dkuid="$(id -u)" \
  --build-arg dkgroup="$(id -gn)" \
  --build-arg dkgid="$(id -g)" \
  .

runtime tag "gnuradio:$DATEVAL" "gnuradio:latest"
