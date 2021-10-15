#!/usr/bin/python3

# read adjacency list
# calculate similarities, contributions
# pass to reducer

import sys

input_m2 = sys.stdin

v_file = open('v', 'r')

page_ranks = dict()
for line in v_file.readlines():
	line = line.strip().split(',')
	page_ranks[int(line[0])] = int(line[1])
	
# print(page_ranks)

for line in input_m2:
	page_no, adj_list = line.split('\t')
	adj_list = adj_list.replace('[','')
	adj_list = adj_list.replace(']','')
	
	adj_list = adj_list.strip('\n')
	adj_list = adj_list.strip()
	adj_list = adj_list.replace(' ','')
	adj_list = adj_list.split(',')
	
	# print(adj_list)
	
	for i in range(0, len(adj_list)):
		adj_list[i] = int(adj_list[i])
	
	len_adj = len(adj_list)
	
	# print(type(adj_list))
		
	page_no = page_no.replace(' ','')
	page_no = int(page_no)
	
	contribution = (page_ranks[page_no]/len(adj_list))
	
	for i in adj_list:
		print(page_no, i, contribution)

