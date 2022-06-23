#!/usr/bin/env python3

import os
import sys
import subprocess


def syntax():
    print("")
    print("Stacker")
    print("------------------------------------------")
    print(" Syntax: stacker <module>")
    print("")

if(sys.argv is not None):
    stack == (sys.argv[1])
    subprocess.call(f"{stack}/run.py")
else: 
    print("Syntax error.")
    syntax()
exit(0)
