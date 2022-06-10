#!/usr/bin/env python3

import os


os.system("wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -")
os.system("sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
os.system("apt update")
os.system("apt install -y jenkins")
print('Jenkins is installed.')
