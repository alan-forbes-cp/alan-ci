#!/usr/bin/env python3 
# Copyright (C) Codeplay Software Limited. All Rights Reserved.
"""Configure and build the ComputeCpp runtime."""

from os import getenv, getcwd, mkdir, chdir, listdir, environ, rename, path
from pathlib import Path
import platform, git, re
#import lib as ci_lib
import random

def main():

    mynum = random.randint(1,2)
    if mynum % 2 == 0:
       exit(1)
    else:
       exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(130)
