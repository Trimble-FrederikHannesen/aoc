#!/usr/bin/python3
import re
import math

i = [l for l in open("input").read().splitlines() if l]

T = [0 if d == 'L' else 1 for d in i[0]]
M = {}
N = []
for n in i[1:]:
	a,b,c = re.findall(r'\w+', n)
	M[a] = [b,c]
	if a[-1]=='A': N.append(a)


C = []
for n in N:
	c = 0
	while not n[-1]=='Z':
		n = M[n][T[c%len(T)]]
		c += 1
	C.append(c)

print(math.lcm(*C))
