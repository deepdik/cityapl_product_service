#!/bin/bash


########### config when only one docker image #############
echo "Starting to deploy docker image.."
DOCKER_IMAGE_WEB=docker-registry.cityapl.com/cityapl_product_service

DOCKER_CRED=cityapl@123

# sudo docker ps -q --filter ancestor=$DOCKER_IMAGE_WEB | xargs -r sudo docker rm -f

git clone https://deepdik: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@github.com/deepdik/cityapl_product_service.git

cd cityapl_product_service

sudo docker-compose down --remove-orphans --rmi 
sudo docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}
sudo docker-compose pull
sudo docker-compose up

###########################################################

# sudo docker run --rm --entrypoint cat ${DOCKER_IMAGE_WEB} docker-compose.yml > docker-compose.yml
# sudo docker-compose pull 
# # sudo docker-compose stop
  
# sudo docker-compose up redis
# sudo docker run  -p 5000:5000 ${DOCKER_IMAGE_WEB}
# sudo docker run  ${DOCKER_IMAGE_CELERY}
# sudo docker run  ${DOCKER_IMAGE_BEAT}
# sudo docker run  ${DOCKER_IMAGE_FLOWER}
