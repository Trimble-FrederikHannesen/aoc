#!/usr/bin/python3
import re

i = [l for l in open("input").read().splitlines() if l]

T = [0 if d == 'L' else 1 for d in i[0]]
M = {}
for n in i[1:]:
	a,b,c = re.findall(r'\w+', n)
	M[a] = [b,c]

n = 'AAA'
c = 0

while not n == 'ZZZ':
	n = M[n][T[c%len(T)]]
	c += 1
print(c)
