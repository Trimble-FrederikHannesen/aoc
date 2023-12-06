#!/usr/bin/python3
def d(x,n):
	return (n-x)*x

def c(x,n,r):
	return d(x,n)>r

def s(n,r):
	return sum(1 for x in range(n) if c(x,n,r))

T,D = [int("".join(l.split()[1:])) for l in open("input").read().splitlines() if l]
C = s(T,D)
print(C)
