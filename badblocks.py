#!usr/bin/env Python

# -*- coding: utf-8 -*-

import os, sys
import subprocess
import commands

#### Hacemos fdisk -l ####

fdisk = commands.getoutput("sudo fdisk -l")
print fdisk

### Solicitamos el dispositivo a reparar ###

# dispositivo = raw_input ("introdusca el dispositivo a reparar")

# dev = dispositivo

repararhd = os.system("sudo badblocks -v -n -f /dev/sdb")

list = (repararhd, dev)
print(repararhd)
