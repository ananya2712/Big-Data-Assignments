#!/usr/bin/python3

# calc new page rank
# send to bash file
# maybe print and delete based on similarity

import sys

filename = sys.argv[1]
f = open(filename,'a')
f.truncate(0)

curr_dest = None
curr_contrib = 0.0

for line in sys.stdin:
	dest,contrib = line.strip().split()
	contrib = float(contrib)
	if curr_dest is not None and curr_dest == dest:
		curr_contrib += contrib 
	else:
		if curr_dest is not None:
			rank = 0.15 + 0.85*curr_contrib
			#print(curr_dest,round(rank,2),sep=",")
			f.write(curr_dest+','+str(round(rank,2))+'\n')
		curr_contrib = contrib 
		curr_dest = dest
		
rank = 0.15 + 0.85*curr_contrib
#print(curr_dest,round(rank,2),sep=",")
f.write(curr_dest+','+str(round(rank,2))+'\n')
f.close()

