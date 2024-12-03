#!/usr/bin/python3
import re

i = open("input").read()
i = re.sub("[\\r\\n]+", " ", i)
i = re.sub("don't\(\).+?do\(\)", "", i)
i = re.findall("mul\(\d{1,3},\d{1,3}\)", i)
i = [re.findall("\d+", m) for m in i]
i = [int(m[0])*int(m[1]) for m in i]
print(sum(i))
