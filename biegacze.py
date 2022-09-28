import math
from sys import stdin
input = stdin.readline

def NWW(n, k):
	return (n * k) // math.gcd(n, k)

def main():
	a, b, c = map(int, input().split())
	nw = NWW(a, b)
	
	print(c // nw)
	
main()
