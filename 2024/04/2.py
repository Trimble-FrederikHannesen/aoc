#!/usr/bin/python3

g = [l for l in open("input").readlines()]
c = 0
for y in range(1,len(g)-1):
	for x in range(1,len(g[y])-1):
		if g[y][x] == 'A':
			d1,d2 = g[y-1][x-1]+g[y+1][x+1],g[y+1][x-1]+g[y-1][x+1]
			if (d1 == "MS" or d1 == "SM") and (d2 == "MS" or d2 == "SM"): c+=1
print(c)
