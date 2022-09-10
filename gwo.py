from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	gwo = list(map(int, input().strip().split()))
	
	while(len(gwo)<n):
		temp_gwo = list(map(int, input().strip().split()))
		gwo.extend(temp_gwo)
		
	
	gwo.sort()

	ile = 0
	maxi = 0
	if k > n:
		print(n)
		return 0
	
	for i in range(n - k - 1):
		if gwo[i] == gwo[i + 1]:
			ile += 1
		else:
			ile = 0
		maxi = max(maxi, ile)
		
	maxi = min(n, maxi + k + 1)
	print(maxi)
	
main()
