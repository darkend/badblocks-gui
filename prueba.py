#!usr/bin/env Python

# -*- coding: utf-8 -*-

import os, sys
import subprocess

repararhd = os.system("sudo badblocks -v -n -f /dev/sda")
print(repararhd)
