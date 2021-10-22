#!/usr/bin/env python3
import sys
current_state=None
current_city=None
current_count=0
state_count = 0
tempc =None
tempco=0
flag=0
for line in sys.stdin:
	line=line.strip()
	word=line.split('+')
	state=word[0]
	city=word[1]
	count=int(word[2])
	if(current_state==state):
		state_count += count
		if(current_city==city):
			current_count+=count
		else:
			if("-" in current_city and city in current_city):
				tempc=current_city
				tempco=current_count
				flag=1
			else:
				print("%s %i" %(current_city, current_count))
				if(flag==1):
					print("%s %i" %(tempc, tempco))
					flag=0
			current_city= city
			current_count= count
	else:
		if current_city:
			print("%s %i" %(current_city, current_count))
		if current_state:
			print("%s %i" %(current_state, state_count))
		current_state= state
		current_city= city
		current_count= count
		state_count= count
		print("%s" %(current_state))
print("%s %i" %(current_city, current_count))
print("%s %i" %(current_state, state_count))
