#!/usr/bin/python3
def d(x,n):
	return (n-x)*x

def c(x,n,r):
	return d(x,n)>r

def s(n,r):
	return sum(1 for x in range(n) if c(x,n,r))

T,D = [[int(x) for x in l] for l in [l.split()[1:] for l in open("input").read().splitlines() if l]]
C = 1
for i in range(len(T)):
	C*=s(T[i],D[i])
print(C)
