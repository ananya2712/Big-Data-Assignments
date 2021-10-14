#!/usr/bin/python3

import sys
import string 

prev_src = None
f = open("v.txt","a")
f.truncate(0)

for line in sys.stdin:
	line = line.strip()
	data = line.split('\t')
	src = data[0]
	dest = data[1]
	if src.isnumeric() and dest.isnumeric():
		print("%s\t%s" %(src,dest))
	
	if prev_src != src:
		f.write(src+','+str(1)+'\n')
		prev_src = src

f.close()

records = list()
filename = 'v.txt'
with open(filename) as fin:
	for line in fin:
		records.append(line.strip())
records.sort()
with open(filename,'w') as fout:
	for line in records: 
		fout.write(line + '\n')
 

