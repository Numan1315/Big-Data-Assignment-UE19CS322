#!/usr/bin/env python3
import json
import sys
pathv=sys.argv[1].strip()
pathe=sys.argv[2].strip()
pagerank = dict()
with open(pathv) as v:
    lines = v.read().strip().split("\n")
    for line in lines:
        try:
            page, rank = line.split(",")
        except:
            continue
        pagerank[page.strip()] = float(rank.strip())
with open(pathe) as e:
	emb=e.read()
	emb=json.loads(emb)
for  line in sys.stdin:
	#page,rank=x.strip().split(',')
	#print(f"{x},{page},{rank}")
	line=line.strip().split('+')
	frm=line[0].strip()
	list1=eval(line[1].strip())
	count = len(list1)
	m = float(pagerank[frm]) / count
	print(f"{frm},{None},{0}")
	for i in list1:
		mul = 0
		z=str(i)
		p=0
		q=0
		for j in range(5):
			mul += emb[frm][j]*emb[z][j]
		for a in emb[frm]:
			p+=a*a
		for b in emb[z]:
			q+=b*b
		p=abs(p**0.5)
		q=abs(q**0.5)
		s =mul/(p*q)
		c=m*s
		print(f"{i},{frm},{c}")
		
				
