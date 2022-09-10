from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	gwo = list(map(int, input().split()))
	
	while(len(gwo)<n):
		temp_gwo = list(map(int, input().strip().split()))
		gwo.extend(temp_gwo)
		
	gwo.sort()
	if k > n:
		print(n)
		return 0
	else:
		c = C(gwo[0 : n - k])

	max_wyn = c.most_common(1)[0][1]
	print(max_wyn + k)
	
main()

