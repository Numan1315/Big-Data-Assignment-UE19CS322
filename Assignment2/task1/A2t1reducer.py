#!/usr/bin/env python3
import sys

l=list()
temp=None
path=sys.argv[1].strip()
try:
	v=open(path,"w")
	for line in sys.stdin:
		line=line.strip().split()
		frm=line[0].strip()
		to=int(line[1].strip())
		if(temp is None):
			temp=frm
			l.append(to)
		else:
			if(temp==frm):
				l.append(to)
			else:
				l.sort()
				print(f"{temp}+{l}")
				v.write("%s,%d\n"%(temp,1))
				temp=frm
				l.clear()
				l.append(to)
	l.sort()
	print(f"{temp}+{l}")
	v.write("%s,%d\n"%(temp,1))
finally:
	v.close()
