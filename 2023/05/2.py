#!/usr/bin/python3

i = [l for l in open("input").read().splitlines() if l]

S = [int(x) for x in i[0].split()[1:]]
S = [range(S[j], S[j]+S[j+1]) for j in range(0, len(S), 2)]

d = {}
M = []
for c in range(2, len(i)):
	if i[c][0].isdigit():
		t,s,l = [int(x) for x in i[c].split()]
		d[range(s,s+l)] = t
	else:
		M.append(d)
		d = {}
M.append(d)

def h(s, m):
	for r in m:
		d = m[r]-r[0]
		if s[0] in r and s[-1] in r:
			return [range(s[0]+d, s[-1]+d+1)]
		elif s[0] not in r and s[-1] in r:
			return [*h(range(s[0], r[0]), m), range(r[0]+d, s[-1]+d+1)]
		elif s[0] in r and s[-1] not in r:
			return [range(s[0]+d, r[-1]+d+1), *h(range(r[-1]+1, s[-1]+1), m)]
	return [s]

for m in M:
	S = [i for l in [h(s, m) for s in S] for i in l]
print(min(r[0] for r in S))
