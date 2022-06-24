#!/usr/bin/env python3

import os


print("Installing requirements.")
os.system("apt update; apt upgrade -y;")
os.system("apt install -y net-tools vim mc htop")
os.system("apt install lsb-release ca-certificates apt-transport-https software-properties-common -y")

print("Setup Repository.")
os.system("wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -")
os.system('echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | '
          'sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list')

print("Install MongoDB.")
os.system("apt update")
os.system("apt install -y mongodb-org")

print("Done.")
