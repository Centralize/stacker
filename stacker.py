#!/usr/bin/env python3

import os
import sys
import subprocess

if(sys.argv is not None):
    stack = sys.argv[1]

subprocess.call(f"{stack}/run.py")
