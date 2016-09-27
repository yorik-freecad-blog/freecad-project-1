#!/usr/bin/env python
import os, sys
import subprocess as sub

with open('temp', 'w+') as F:
	sub.call(['date'], stdout=F)
	F.seek(0)
	line=F.readline()
print(line)
os.remove('temp')