#!/bin/bash

#
# Kali Docker Setup Script
# @decidedlygray 20180902
# LICENSE: MIT
#

# Steps taken from: https://docs.docker.com/install/linux/docker-ce/debian/
# And: https://medium.com/@airman604/installing-docker-in-kali-linux-2017-1-fbaa4d1447fe
# Install uses the repository, so we can get updates in the future

# Remove any existing docker packages and update package list
sudo apt remove docker docker-engine docker.io -y
sudo apt update

# Install apt HTTPS packages
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
# Verify key exists
# sudo apt-key fingerprint 0EBFCD88

# Add stable repo
# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian jessie stable"
echo 'deb https://download.docker.com/linux/debian stretch stable' > /etc/apt/sources.list.d/docker.list

# Update repo list
sudo apt update

# Finally, install Docker Community Edition
sudo apt install docker-ce -y
# Verify install by running the docker hello world
systemctl start docker
sudo docker run hello-world
