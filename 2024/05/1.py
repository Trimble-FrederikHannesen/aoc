#!/usr/bin/python3
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
		if f:
			C+=int(s[len(s)//2])
print(C)
