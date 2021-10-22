#!/usr/bin/env python3

import json
import sys
from datetime import datetime 
count=0
def checkDescription(line):
	desc=["lane blocked","shoulder blocked","overturned vehicle"]
	for i in desc:
		if i in line['Description'].lower():
			return 1
	return 0

def checkWheather(line):
	weather=["Heavy Snow","Thunderstorm","Heavy Rain","Heavy Rain Showers","Blowing Dust"]
	for i in weather:
		if (i == line["Weather_Condition"]):
			return 1
	return 0


for line in sys.stdin:
	line=json.loads(line)
	date=line['Start_Time']
	if(checkDescription(line) and line["Severity"]>=2 and line["Sunrise_Sunset"]=="Night" and line["Visibility(mi)"]<=10 and line["Precipitation(in)"]>=0.2 and checkWheather(line)):
		date=line['Start_Time']
		l1=date.split(':')
		dobj=datetime.strptime(l1[0],"%Y-%m-%d %H")
		print('%d %s' %(dobj.hour,1))
