#!/usr/bin/python3
from operator import sub
i = [list(map(int, l.split())) for l in open("input").readlines()]
i = [list(map(sub, l, l[1:])) for l in i]
r = 0
for l in i:
	if abs(l[0]) < 1 or abs(l[0]) > 3: continue
	d = l[0]/abs(l[0])
	s = True
	for e in l:
		if abs(e) < 1 or abs(e) > 3:
			s = False
			break
		dE = e/abs(e)
		if dE != d:
			s = False
			break
	if s:
		r += 1
print(r)

