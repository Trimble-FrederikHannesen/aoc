#!/usr/bin/python3
from functools import cmp_to_key


def t(c):
	S = [[5], [1,4], [2,3], [1,1,3], [1,2,2], [1,1,1,2], [1,1,1,1,1]]
	return S.index(sorted([*{k:c.count(k) for k in c}.values()]))

def s(h,g):
	x = [i for i in range(len(h[0])) if h[0][i]!=g[0][i]][0]
	return -1 if sorted([h,g], key=lambda e: (t(e[0]), 'AKQJT98765432'.index(e[0][x])))[0] == g else 1

H = sorted([l.split() for l in open("input").read().splitlines() if l], key=cmp_to_key(s))
print(sum(int(H[i][1]) * (i+1) for i in range(len(H))))
