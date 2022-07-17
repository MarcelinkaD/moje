from sys import stdin
from collections import Counter
input = stdin.readline

def main():
	n = int(input())
	liczby = list(map(int, input().split()))
	c = Counter(liczby)
	
	if n % 2 == 0:
		for i in c:
			if c[i] % 2 == 1:
				return "NIE"
		
		return "TAK"
	else:
		k = 0
		for i in c:
			if c[i] % 2 == 1:
				k += 1
			
		if k == 1:
			return "TAK"
		else:
			return "NIE"

print(main())
