#!usr/bin/env Python

# -*- coding: utf-8 -*-

# Reparador de Discos Duros

import sys
import os

import subprocess
import commands
from PyQt4 import QtCore, QtGui, uic

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("badblocks-gui.ui")[0]

### Hacemos fdisk -l e imprimimos resulatdos en pantalla ####
fdisk = commands.getoutput("sudo fdisk -l")
print fdisk

### Solicitamos el dispositivo a reparar. Omitimos el /dev/ ###
dispositivo = raw_input ("introdusca el dispositivo a reparar.(sda, sdc, omita el /dev/)")
dev = dispositivo

# Preguntamos si desea hacerlo en modo destructivo.
destructivo = raw_input ("Desea hacerlo en Modo destructivo S/N")
d = destructivo

### Declaramos el comando a utilizar. Modo no destructivo.
repararhd = os.system("sudo badblocks -v -n -s -f /dev/" + dev)

### Declaramos el comando a utilizar. Modo destructivo.
repararhdd = os.system("sudo badblocks -v -w -s -f /dev/" + dev)

#Declaramos condicional
if d == N:
	print repararhdd
else: 
	print repararhd










