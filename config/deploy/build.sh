#!/bin/bash

echo "Starting to deploy docker image.."
DOCKER_IMAGE=docker-registry.cityapl.com/cityapl_product_service
docker pull $DOCKER_IMAGE
docker ps -q --filter ancestor=$DOCKER_IMAGE | xargs -r docker stop
docker run -d -p 5000:5000 $DOCKER_IMAGE