#!/usr/bin/env python3

import sys
import json 
import math
import requests

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
d = float(sys.argv[3])

def euclid_dist(line):
	 dist = (latitude-float(line['Start_Lat']))**2 +(longitude-float(line['Start_Lng']))**2
	 dist = dist**0.5
	 return dist
	 
for line in sys.stdin:
	line = json.loads(line)
	
	if line['Start_Lat'] and line['Start_Lng']:
		dist = euclid_dist(line)
		if dist > d:
			continue
		else:
			payload = {"latitude": line['Start_Lat'],"longitude":line['Start_Lng']}
			response = requests.post(url = "http://20.185.44.219:5000/", json = payload)
			print(response.json()['state'],",",response.json()['city'],",",1)
		
	

