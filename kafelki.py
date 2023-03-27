import math
from sys import stdin
input = stdin.readline

def main():
	n, q = map(int, input().split())
	l = list(map(int, input().split()))
	maxi = max(l)
	zlicz = [0 for _ in range(maxi + 1)]
	
	for i in range(n):
		zlicz[l[i]] += 1
	
	w = [0 for i in range(maxi + 1)]
	for i in range(1, maxi + 1):
		for j in range(i, maxi + 1, i):
			w[j] += zlicz[i]
	
	for _ in range(q):
		a, b = map(int, input().split())
		breakpoint()
		print(w[math.gcd(a, b)])
		
		
	
main()
