#!/bin/bash
docker build -t gnr-sid --build-arg dkuser=$(id -un) --build-arg dkgroup=$( id -gn) .
