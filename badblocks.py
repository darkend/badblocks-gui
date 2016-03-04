#!usr/bin/env Python

# -*- coding: utf-8 -*-

import os, sys
import subprocess
import commands

#### Hacemos fdisk -l ####

fdisk = commands.getoutput("sudo fdisk -l")
print fdisk

### Solicitamos el dispositivo a reparar ###

dispositivo = raw_input ("introdusca el dispositivo a reparar.(sda, sdc, omita el /dev/)")

dev = dispositivo


### Declaramos el comando a utilizar

repararhd = os.system("sudo badblocks -v -n -f /dev/" + dev)

print repararhd

