#!/usr/bin/python3

l = [i.split() for i in open("input").readlines()]
r = sorted([int(i[1]) for i in l])
l = sorted([int(i[0]) for i in l])
s = 0
for i in l:
	s += i * r.count(i)
print(s)
