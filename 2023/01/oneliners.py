#!/usr/bin/python3
import re

print(sum([int(re.sub(r'^[^\d]*(\d).*$', r'\1', l) + re.sub(r'^.*(\d)[^\d]*', r'\1', l)) for l in open("input").read().splitlines() if l]))

print(sum([int(re.sub(r'^[^\d]*(\d).*$', r'\1', l) + re.sub(r'^.*(\d)[^\d]*$', r'\1', l)) for l in [l.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine') for l in open("input").read().splitlines() if l]]))
