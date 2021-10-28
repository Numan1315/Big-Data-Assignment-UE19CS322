#!/usr/bin/env python3
import sys

for line in sys.stdin:
	line=line.strip().split()
	from_node=line[0].strip()
	to_node=line[1].strip()
	print("%s\t%s" %(from_node,to_node))
