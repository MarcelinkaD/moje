from sys import stdin
import math
input = stdin.readline

def main():
	n, k = map(int, input().split())
	w = n // math.gcd(n, k)
	print(w)
	
main()
