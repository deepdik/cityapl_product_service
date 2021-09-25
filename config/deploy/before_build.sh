#!/bin/bash

echo "Starting before build.."


# install docker, docker-compose and other dependency

sudo groupadd docker
sudo usermod -aG docker $USER
