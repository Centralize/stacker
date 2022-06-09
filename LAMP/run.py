#!/usr/bin/env python3

import os
import subprocess
import socket


def checkRoot():
    try:
        os.rename('/root/.bash_history', '/root/.bash_history')
    except Exception():
        if (e[0] is errno.EPERM):
            sys.exit("You need to run as root or sudo. Exiting.")


os.system("apt update; apt upgrade -y;")
os.system("apt install -y net-tools")

apachePresent = os.system("netstat -lnput | grep \":80\" | grep \"LISTEN\" | cut -d '/' -f 2")
if(apachePresent is None):
    os.system("apt install -y apache2")
else:
    print("Apache2 is already installed.")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipaddress = s.getsockname()[0]
s.close()


