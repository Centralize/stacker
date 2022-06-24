#!/usr/bin/env python3

import subprocess
import sys


def syntax():
    print("")
    print("Stacker")
    print("------------------------------------------")
    print(" Syntax: stacker <module>")
    print("")

try:
    stack == (sys.argv[1])
    subprocess.call(f"{stack}/run.py")
except:
    print("Syntax error.")
    syntax()
exit(0)
