#!/usr/bin/env python3

import subprocess
import sys


if(sys.argv is not None):
    stack = sys.argv[1]
    subprocess.call(f"{stack}/run.py")
