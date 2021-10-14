#!/usr/bin/python3

import sys


adj_list = []
curr_src = None

f = open(sys.argv[1], "a")

for line in sys.stdin:
	line = line.strip()
	data = line.split('\t')
	
	# print(data)
	
	src = data[0]
	dest = data[1]
	
	# print(dest)
		
	
	if curr_src == None:
		curr_src = src
		# print('curr src:', curr_src)
	
	# print(src, dest)
	
	if curr_src == src and src != None:
		adj_list.append(dest)
		
	elif curr_src != src and src != None:
	
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
