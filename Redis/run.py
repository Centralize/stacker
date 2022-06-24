#!/usr/bin/env python3

import os
import subprocess
from os import path


def checkRoot():
    try:
        os.rename('/root/.bash_history', '/root/.bash_history')
    except Exception():
        if (e[0] is errno.EPERM):
            sys.exit("You need to run as root or sudo. Exiting.")


os.system("apt update; apt upgrade -y;")
os.system("apt install -y net-tools vim mc htop")
os.system("apt install lsb-release ca-certificates apt-transport-https software-properties-common -y")

os.system("apt install -y redis-server")
os.system("sed -i 's/supervised no/supervied systemd/g' /etc/redis/redis.conf")
os.system("systemctl restart redis.service")
os.system("systemctl status redis")
os.system("systemctl enable redis")