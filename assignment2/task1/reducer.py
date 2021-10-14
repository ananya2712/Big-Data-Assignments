#!/usr/bin/python3

import sys


adj_list = []
curr_src = None

f=open(sys.argv[1],"a")

for line in sys.stdin:
	line = line.strip()
	data = line.split('\t')
	src , dest = data
	
	if curr_src == None:
		curr_src = src
		
	if curr_src == src and src != None:
		flag = 0
		for i in range(len(adj_list)):
			if adj_list[i] < dest :
				continue
			else:
				adj_list.insert(i,dest) #insert the dest at index i	
				flag = 1
				break
			
		if(flag == 0):
			adj_list.append(dest)
		
	elif curr_src != src and src != None:
		
		print(curr_src,'\t') #stuff to make a adj list ->hdfs 
		print("[", end="")
		
		for node in range(len(adj_list)): #formatting for printing the adj list

			if(node == len(adj_list)-1):
				print(adj_list[node], end="")

			else:
				print(adj_list[node],",", end=" ")
		print(']')
		
		curr_src = src #update the curr_src
		adj_list = []

if curr_src==src:
		print(curr_src,'\t')
		print("[", end="")
		
		length = len(adj_list)

		for node in range(length):

			if(node == length-1):
				print(adj_list[node], end="")

			else:
				print(adj_list[node], ",", end=" ")

		print("]")
		
		
		
		
	
	
	
