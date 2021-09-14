#!/usr/bin/env python3

import sys

outputs = {}
for line in sys.stdin:
	line = line.strip()
	words = line.split(" , ")
	words[1] = words[1].strip('\n')
	
	if words[0] in outputs.keys():
		if words[1] not in outputs[words[0]].keys() :
			outputs[words[0]][words[1]] = 1 
		else:
			outputs[words[0]][words[1]] += 1
	else:
		outputs[words[0]] = {}
		outputs[words[0]][words[1]] = 1 

for i in outputs.keys():
	print(i)
	count=0
	for j in outputs[i].keys():
		print(j,outputs[i][j])
		count = count + outputs[i][j]
	print (i,count)
	
	
		
		
			
	
