#!/usr/bin/python3
from operator import sub
i = [list(map(int, l.split())) for l in open("input").readlines()]
r = 0

def c(l):
	l = list(map(sub, l, l[1:]))
	if abs(l[0]) < 1 or abs(l[0]) > 3: return False
	d = l[0]/abs(l[0])
	for e in l:
		if abs(e) < 1 or abs(e) > 3: return False
		dE = e/abs(e)
		if dE != d: return False
	return True

for l in i:
	if c(l): r += 1
	else:
		for i in range(len(l)):
			k = l[:i] + l[i+1:]
			if c(k):
				r+= 1
				break
print(r)

