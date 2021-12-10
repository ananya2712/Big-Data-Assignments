#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	data = line.split('\t')
	src = data[0]
	dest = data[1]
	if src.isnumeric() and dest.isnumeric():
		print("%s\t%s" %(src,dest))
