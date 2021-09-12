#!/usr/bin/env python3

import datetime
import sys
import json 
import ast

output = {}

for line in sys.stdin:	
	line=line.strip()
	words = line.split()
	for word in words:
		if '-' not in word:
			time = word.split(':')
			if time[0] not in output.keys():
				output[time[0]] = 1
			else:
				output[time[0]] = output[time[0]] + 1
				
for i in sorted(output):
    print (i, output[i])
	
	
	

