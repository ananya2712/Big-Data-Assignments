#!/usr/bin/env python3

import sys
import json 
import math
import requests
url_req ="http://20.185.44.219:5000/"

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
d = float(sys.argv[3])
	 
for line in sys.stdin:
	line = line.strip()
	line = json.loads(line)
	try:
		lat = float (line['Start_Lat'])
		lng = float (line['Start_Lng'])

		if math.isnan(lat) or math.isnan(lng):
			continue
			
		dist = (latitude-float(line['Start_Lat']))**2 +(longitude-float(line['Start_Lng']))**2
		dist = dist**0.5
		
		if dist <= d:
			payload = {"latitude": lat,"longitude":lng}
			response = requests.post(url = url_req, json = payload)
			response = response.json()
			res_state = str(response['state'])
			res_city = str(response['city'])
			print('%s,%s,%s' %(res_state,res_city,1))
	except:
		continue
		
	

