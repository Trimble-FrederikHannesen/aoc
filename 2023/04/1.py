#!/usr/bin/python3

print(sum(int(2**(len(set(s[0].split()).intersection(set(s[1].split())))-1)) for s in [l[l.index(": ")+1:].split(" | ") for l in open("input").read().splitlines() if l]))
