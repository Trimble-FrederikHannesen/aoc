#!/usr/bin/python3
import re

print(sum([int(re.sub(r'^[^\d]*(\d).*$', r'\1', l) + re.sub(r'^.*(\d)[^\d]*', r'\1', l)) for l in open("input").read().splitlines() if l]))
