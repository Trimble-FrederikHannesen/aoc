#!/usr/bin/python3
import re

print(sum(max(int(d) for d in re.findall(' \d+(?= red)', l))*max(int(d) for d in re.findall(' \d+(?= green)', l))*max(int(d) for d in re.findall(' \d+(?= blue)', l)) for l in open("input").read().splitlines() if l))
