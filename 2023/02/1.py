#!/usr/bin/python3
import re

print(sum([int(re.sub(r'^.+ (\d+):.+$', r'\1', l)) for l in open("input").read().splitlines() if l and max(int(d) for d in re.findall(' \d+(?= red)', l))<=12 and max(int(d) for d in re.findall(' \d+(?= green)', l))<=13 and max(int(d) for d in re.findall(' \d+(?= blue)', l))<=14]))
