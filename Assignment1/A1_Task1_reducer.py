#!/usr/bin/env python3

import sys


dic={}
for line in sys.stdin:
	line=line.strip()
	word=line.split(' ')
	count=int(word[1])
	key=int(word[0])
	try:
		dic[key].append(count)
	except KeyError:
		dic[key]=[count]
		continue

for i in sorted(dic.keys()):
	dic[i]=sum(dic[i])
	print("%d %d" %(i,dic[i]))
