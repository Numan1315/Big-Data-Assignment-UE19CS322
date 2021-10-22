#!/usr/bin/env python3
import json
import sys
import requests

url = "http://20.185.44.219:5000/"
given_lat=int(sys.argv[1])
given_long=int(sys.argv[2])

for line in sys.stdin:
	line=json.loads(line)
	lat_time=line['Start_Lat']
	long_time=line['Start_Lng']
	x=(given_lat - lat_time)**2
	y=(given_long - long_time)**2
	dist = (x+y)**0.5
	D=float(sys.argv[3])
	if(dist <= D):
		data ={
    			'latitude' : lat_time ,
    			'longitude' : long_time
			}

		r = requests.post(url = url, json=  data)
		output = r.json()
		state=output["state"]
		city=output["city"]
		print("%s:%s:%d" %(state,city,1))
	else:
		continue
