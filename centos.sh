#!/bin/bash

# Setup repository
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Install docker and docker compose
sudo yum install docker-ce docker-ce-cli docker-compose-plugin

# Start docker service
sudo systemctl start docker

# Add system user to docker group
sudo usermod -aG docker $USER