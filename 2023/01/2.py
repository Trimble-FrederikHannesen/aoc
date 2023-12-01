#!/usr/bin/python3

def get(l, dir):
	m = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for x in range(0 if dir > 0 else 1, len(l) if dir >0 else len(l) + 1):
		if l[dir * x].isdigit():
			return l[dir * x]
		for n in m:
			if l[dir * x:].startswith(n):
				return str(m.index(n))
	assert False, "no digit in " + l

print(sum([int(get(l, 1) + get(l, -1)) for l in open("input").read().splitlines() if l]))
