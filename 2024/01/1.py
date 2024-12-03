#!/usr/bin/python3

l = [i.split() for i in open("input").readlines()]
r = sorted([int(i[1]) for i in l])
l = sorted([int(i[0]) for i in l])
d = sum([abs(l[i]-r[i]) for i in range(len(l))])
print(d)
