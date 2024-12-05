#!/usr/bin/python3
from functools import cmp_to_key

def cmp(l,r):
	if l in R and r in R[l]: return 1
	if r in R and l in R[r]: return -1
	return 1

R = dict()
C = 0
for l in [l.strip() for l in open("input").readlines()]:
	if "|" in l:
		f,s = l.split("|")
		if s not in R: R[s] = set()
		R[s].add(f)
	elif "," in l:
		s = l.split(",")
		p = set()
		f = True
		for o in s:
			if o in R:
				t = set(s)
				t.remove(o)
				if not R[o].intersection(t).issubset(p):
					f = False
					break
			p.add(o)
		if not f:
			C+=int(sorted(s, key=cmp_to_key(cmp))[len(s)//2])
print(C)
