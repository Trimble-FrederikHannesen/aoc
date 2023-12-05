#!/usr/bin/python3

i = [l for l in open("input").read().splitlines() if l]

S = [int(x) for x in i[0].split()[1:]]
d = {}
m = []
for c in range(2, len(i)):
	if i[c][0].isdigit():
		t,s,l = [int(x) for x in i[c].split()]
		d[range(s,s+l)] = t
	else:
		m.append(d)
		d = {}
m.append(d)
for k in m:
	for i in range(len(S)):
		for r in k:
			if S[i] in r:
				S[i] = S[i]-r.start + k[r]
				break
print(min(S))
