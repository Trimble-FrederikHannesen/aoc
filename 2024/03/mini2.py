#!/usr/bin/python3
import re

print(sum(int(m[0])*int(m[1]) for m in [re.findall("\d+", m) for m in re.findall("mul\(\d{1,3},\d{1,3}\)", re.sub("don't\(\).+?do\(\)", "", re.sub("[\\r\\n]+", " ", open("input").read())))]))
