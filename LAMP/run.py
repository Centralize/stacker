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

ondrejPresent = path.exists("/etc/apt/sources.list.d/ondrej-ubuntu-php-focal.list")
if(ondrejPresent is False):
    os.system("add-apt-repository ppa:ondrej/php")
else:
    print("PHP 8.1 Repository is already installed.")

os.system("apt update;")

apachePresent = os.system("service apache2 status")
if(apachePresent > 0):
    os.system("apt install -y apache2 php8.1 php8.1-cli ")
else:
    print("Apache2 is already installed.")

mysqlPresent = os.system("service mysql status")
if(apachePresent > 0):
    os.system("apt install -y mysql-server mysql-client")
else:
    print("MySQL is already installed.")

phpPresent = path.exists("/etc/php")
if(phpPresent is not True):
    os.system("apt install -y php8.1-imagick php8.1-imap php8.1-mysql")
else:
    print("PHP 8.1 is already installed.")

