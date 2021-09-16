#!/usr/bin/env python3

import sys
import json
import math
import requests
url_req = "http://20.185.44.219:5000/"

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
d = float(sys.argv[3])

for line in sys.stdin:
    try:
        line = line.strip()
        line = json.loads(line)
        lat = float(line['Start_Lat'])
        lng = float(line['Start_Lng'])

        if math.isnan(lat) or math.isnan(lng):
            continue

        dist = (latitude - lat)**2 + \
            (longitude - lng)**2
        dist = dist**0.5

        if dist <= d:
            payload = {"latitude": lat, "longitude": lng}
            response = requests.post(url=url_req, json=payload)
            response = response.json()  # json.loads(response.text)
            res_state = response['state']
            res_city = response['city']
            print(f"{res_state}, {res_city}, 1")
    except BaseException:
        continue
