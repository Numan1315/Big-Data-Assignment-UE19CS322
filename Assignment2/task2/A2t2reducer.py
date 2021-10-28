#!/usr/bin/env python3
import sys
temp=None
rank=0.15
for  line in sys.stdin:
	line=line.strip().split(',')
	dest=line[0].strip()
	src=line[1].strip()
	c=float(line[2].strip())
	if(temp==None):
		temp=dest
		rank+=0.85*c
	elif(temp==dest):
		rank+=0.85*c
	else:
		print(f"{temp},{rank:.2f}")
		temp=dest
		rank=0.15+0.85*c
print(f"{temp},{rank:.2f}")
