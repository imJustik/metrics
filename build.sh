#!/bin/bash

docker build -t api ./flask
docker build -t grafana ./grafana
docker build -t graphite ./graphite
docker build -t nginx ./nginx


docker-compose up -d
