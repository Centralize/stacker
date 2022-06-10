#!/usr/bin/env python3

import os
from os import path
import subprocess
import socket


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


jenkinsPresent = os.system("service status jenkins")
if(jenkinsPresent is False):
    os.system("wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -")
    os.system("sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
    os.system("apt update")
    os.system("apt install -y jenkins")
else:
    print("Jenkins is already installed.\n")

jenkinsPresent = os.system("service status jenkins")
if(jenkinsPresent is True):
    print(f'Jenkins is installed. Access GUI @: http://{local_ip}:8080')
