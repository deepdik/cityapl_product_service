#!/bin/bash


echo "Starting to deploy docker image.."
SERVICE_NAME = cityapl_product_service
DOCKER_IMAGE_WEB=docker-registry.cityapl.com/${SERVICE_NAME}

DOCKER_CRED=cityapl@123
GIT_CRED = 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

rm -rf ${SERVICE_NAME}
git clone https://deepdik:${GIT_CRED}@github.com/deepdik/${SERVICE_NAME}.git

cd ${SERVICE_NAME}

sudo docker-compose down --remove-orphans --rmi 
sudo docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}
sudo docker-compose pull
sudo docker-compose up -d

###########################################################
