#!/usr/bin/python3

i = [len(set(s[0].split()).intersection(set(s[1].split()))) for s in [l[l.index(": ")+1:].split(" | ") for l in open("input").read().splitlines() if l]]
d = {n:1 for n in range(1, len(i)+1)}
for n in range(1, len(i)+1):
	for v in range(1, i[n-1]+1):
		d[n+v] += d[n]
print(sum(d.values()))
