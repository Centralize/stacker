#!/usr/bin/env python3

import os
import subprocess


def checkRoot():
    try:
        os.rename('/root/.bash_history', '/root/.bash_history')
    except Exception():
        if (e[0] is errno.EPERM):
            sys.exit("You need to run as root or sudo. Exiting.")


os.system("apt update; apt upgrade -y;")
os.system("apt install -y net-tools vim mc htop")

apachePresent = os.system("service apache2 status")
if(apachePresent > 0):
    os.system("apt install -y apache2")
else:
    print("Apache2 is already installed.")

mysqlPresent = os.system("service mysql status")
if(apachePresent > 0):
    os.system("apt install -y mysql-server mysql-client")
else:
    print("MySQL is already installed.")

