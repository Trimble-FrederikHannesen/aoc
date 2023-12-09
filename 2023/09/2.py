#!/usr/bin/python3

i = [[int(x) for x in l.split()] for l in open("input").read().splitlines() if l]

def v(l):
	if not any(l): return 0
	return l[-1]+v([l[i+1]-l[i] for i in range(len(l)-1)])

print(sum(v(l[::-1]) for l in i))
