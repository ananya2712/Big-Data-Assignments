#!/usr/bin/python3

import sys
import string 

prev_src = None
filename = sys.argv[1]
f = open(filename,'a')
f.truncate(0)

adj_list = []
curr_src = None

for line in sys.stdin:
	line = line.strip()
	data = line.split('\t')
	
	src = data[0]
	dest = data[1]
	
	if curr_src == None:
		curr_src = src
		f.write(src+','+str(1)+'\n')
	
	if curr_src == src and src != None:
		adj_list.append(dest)
		
	elif curr_src != src and src != None:
		f.write(src+','+str(1)+'\n')
		print(curr_src,'\t', "[", end="")
		for node in range(len(adj_list)):
			if(node == len(adj_list)-1):
				print(adj_list[node], end="")
			else:
				print(adj_list[node], ",", end=" ")
		print("]")
		
		curr_src = src #update the curr_src
		adj_list = []
		
		flag = 0
		for i in range(len(adj_list)):
			adj_list.insert(i, dest) #insert the dest at index i	
			# print('adj:', adj_list)
			flag = 1
			break
			
		if(flag == 0):
			adj_list.append(dest)

print(curr_src,'\t', "[", end="")
for node in range(len(adj_list)):
	if(node == len(adj_list)-1):
		print(adj_list[node], end="")
	else:
		print(adj_list[node], ",", end=" ")
print("]")

f.close()
records = list()
#filename = 'v.txt'
with open(filename) as fin:
	for line in fin:
		records.append(line.strip())
records.sort()
with open(filename,'w') as fout:
	for line in records: 
		fout.write(line + '\n')
