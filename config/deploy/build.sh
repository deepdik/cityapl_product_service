#!/bin/bash


########### config when only one docker image #############
echo "Starting to deploy docker image.."
DOCKER_IMAGE=docker-registry.cityapl.com/cityapl_product_service
DOCKER_CRED=cityapl@123

sudo docker ps -q --filter ancestor=$DOCKER_IMAGE | xargs -r sudo docker stop
sudo docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}
sudo docker pull ${DOCKER_IMAGE}

###########################################################

############### config for docker-compose ##################

docker run -it ${DOCKER_IMAGE} bash
sudo docker-copose up