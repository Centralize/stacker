#!/usr/bin/env python3

import os
import sys
import subprocess
import paramiko
from settings import *


if(sys.argv is not None):
    contype = sys.argv[2]

if contype == "module":
    stack == (sys.argv[3])
    subprocess.call(f"{stack}/run.py")
elif contype == "remote":
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sys.argv[3],ssh_port,ssh_username,ssh_password,timeout=10)
    stdin,stdout,stderr = ssh.exec_command("pwd")
    result = stdout.read()
    print(result)
    ssh.close()
exit(0)
