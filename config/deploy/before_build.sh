#!/bin/bash

echo "Starting before build.."


# install docker, docker-compose and other dependency

sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version


sudo groupadd docker
sudo usermod -aG docker $USER
