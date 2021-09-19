#!/bin/bash

echo "Starting to deploy docker image.."
DOCKER_IMAGE=docker-registry.cityapl.com/cityapl_product_service
DOCKER_CRED=cityapl@123
sudo docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}
sudo docker ps -q --filter ancestor=$DOCKER_IMAGE | xargs -r docker stop
sudo docker pull $DOCKER_IMAGE
sudo docker run -d -p 5000:5000 $DOCKER_IMAGE
