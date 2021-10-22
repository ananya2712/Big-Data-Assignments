#!/usr/bin/python3

# read adjacency list
# calculate similarities, contributions
# pass to reducer

import sys
import json 
import math

input_m2 = sys.stdin

filename = sys.argv[1]
v_file = open(filename, 'r')

filename_json = sys.argv[2]
embedding = open(filename_json,)
data = json.load(embedding)

#dot product without numpy
def dot(v1, v2):
	nom_v1 = math.sqrt(sum(i*i for i in v1))
	nom_v2 = math.sqrt(sum(i*i for i in v2))
	return sum(x*y for x, y in zip(v1, v2))/(nom_v1*nom_v2)

page_ranks = dict()
for l in v_file.readlines():
	l = l.strip().split(',')
	page_ranks[int(l[0])] = int(l[1].strip())
	
for line in input_m2:
	page_no, adj_list = line.split('\t')
	adj_list = adj_list.replace('[','')
	adj_list = adj_list.replace(']','')
	
	adj_list = adj_list.strip('\n')
	adj_list = adj_list.strip()
	adj_list = adj_list.replace(' ','')
	adj_list = adj_list.split(',')
	
	page_no = page_no.replace(' ','')
	page_no = int(page_no)
	print(page_no,0,sep=',')
	
	for i in range(0, len(adj_list)):
		adj_list[i] = int(adj_list[i])
	
	len_adj = len(adj_list)
	if len(adj_list) == 0:
		continue
	try:
		contribution = (page_ranks[page_no]/len(adj_list))
	except KeyError: 
		continue
	except ValueError:
		continue
	
	for i in adj_list:
		sim = dot(data[str(page_no)],data[str(i)])
		c = contribution*sim*page_ranks[page_no]
		print(i,c,sep=',')
embedding.close()
v_file.close()
