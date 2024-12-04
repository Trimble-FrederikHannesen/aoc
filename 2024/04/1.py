#!/usr/bin/python3

g = [l for l in open("input").readlines()]
c = 0
for y in range(len(g)):
	for x in range(len(g[y])):
		for dY in [-1,0,1]:
			for dX in [-1,0,1]:
				if y+3*dY < 0 or x+3*dX < 0 or y+3*dY >= len(g) or x+3*dX >= len(g[y]): continue
				if g[y][x]+g[y+dY][x+dX]+g[y+2*dY][x+2*dX]+g[y+3*dY][x+3*dX] == "XMAS": c+=1
print(c)
