#!/usr/bin/env python3

import json
import sys

output = {}
for line in sys.stdin:
	data = json.loads(line)
	if (data['Severity']>=2 and data['Sunrise_Sunset']=='Night' and data['Visibility(mi)'] <= 10 and data['Precipitation(in)'] > 0.2 ):
		if(data['Weather_Condition'] in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers", "Blowing Dust"]):
			if("lane blocked" in data['Description'] or "shoulder blocked" in data['Description'] or "overturned vehicle" in data['Description']):
				print(line,",")
	
	
	 
		
	
		
	
	
	
	
