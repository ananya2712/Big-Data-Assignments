#!/usr/bin/env python3

import datetime
import sys
import json 
import ast

output = {}

for line in sys.stdin:	
	line=line.strip()
	#temps = line.split(',')
	words = line.split()
	for word in words:
		if ':' in word and '-' not in word:
			time = word.split(':')
			t = int(time[0])
			if t not in output.keys():
				output[t] = 1
			else:
				output[t]=output[t] + 1
				
for i in sorted(output):
    print (i, output[i])
	
	
	

