#!/bin/bash


########### config when only one docker image #############
echo "Starting to deploy docker image.."
DOCKER_IMAGE_WEB=docker-registry.cityapl.com/cityapl_product_service
DOCKER_IMAGE_CELERY=docker-registry.cityapl.com/celery_worker_cityapl_product_service
DOCKER_IMAGE_BEAT=docker-registry.cityapl.com/celery_beat_cityapl_product_service
DOCKER_IMAGE_FLOWER=docker-registry.cityapl.com/celery_flower_cityapl_product_service
DOCKER_CRED=cityapl@123

sudo docker ps -q --filter ancestor=$DOCKER_IMAGE_WEB | xargs -r sudo docker rm -f
sudo docker ps -q --filter ancestor=$DOCKER_IMAGE_CELERY | xargs -r sudo docker rm -f
sudo docker ps -q --filter ancestor=$DOCKER_IMAGE_BEAT | xargs -r sudo docker rm -f
sudo docker ps -q --filter ancestor=$DOCKER_IMAGE_FLOWER | xargs -r sudo docker rm -f

sudo docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}
sudo docker pull ${DOCKER_IMAGE_WEB}

###########################################################

sudo docker run --rm --entrypoint cat ${DOCKER_IMAGE_WEB} docker-compose.yml > docker-compose.yml
sudo docker-compose pull 
# sudo docker-compose stop
  
sudo docker-compose up redis
sudo docker run  -p 5000:5000 ${DOCKER_IMAGE_WEB}
sudo docker run  ${DOCKER_IMAGE_CELERY}
sudo docker run  ${DOCKER_IMAGE_BEAT}
sudo docker run  ${DOCKER_IMAGE_FLOWER}
