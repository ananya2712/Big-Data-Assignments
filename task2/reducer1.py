#!/usr/bin/env python3

import sys

current_state = None 
current_city = None
current_count = 0
total_count = 0 

for line in sys.stdin:
	line = line.strip()
	state , city , count = line.split(',')

	try:
		count = int(count)
	except ValueError:
		continue
	if current_state == None:
		print(state)
	if current_state == state or current_state == None:
		total_count +=count
		
	if current_state!= state or current_city!=city:
		if current_city != None:
			print(current_city,current_count)
		
		if current_state != state and current_state != None:
			print(current_state,total_count)
			total_count = 0 
			print(state)
			
		
		current_state = state 
		current_city = city
		current_count = count
	else:
		current_count+=count
		
print(current_city,current_count)
total_count += current_count		
if current_state:
	print(current_state,total_count)	
		
	
	
	
