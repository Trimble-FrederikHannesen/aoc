#!/usr/bin/python3
import re
g = [l for l in open("input").read().splitlines() if l]
c = 0
n = {}
for y in range(len(g)):
        for x in range(len(g[y])):
                if not g[y][x].isdigit() and not g[y][x] == '.':
                        for dy in [-1,0,1]:
                                for dx in [-1,0,1]:
                                        if y+dy<0 or y+dy>=len(g) or x+dx<0 or x+dx>=len(g[y]):
                                                continue
                                        if g[y+dy][x+dx].isdigit():
                                                while x+dx-1>=0 and g[y+dy][x+dx-1].isdigit():
                                                        dx-=1
                                                n[(y+dy,x+dx)] = int(re.sub(r'^(\d+).*$', r'\1', g[y+dy][x+dx:]))
for k in n:
        c += n[k]
print(c)
