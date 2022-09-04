from sys import stdin
input = stdin.readline
import math

def czy_pierwsza(p):
	for i in range(2, int(math.sqrt(p)) + 1):
		if p % i == 0:
			return False
	
	return True
	
def czy_Gold(h):
	for i in range(2, int(math.sqrt(h)) + 1):
		if czy_pierwsza(i) and czy_pierwsza(h - i):
			return True
	
	return False

def main():
	n = int(input())
	if n == 1 or czy_pierwsza(n):
		return 1
	elif czy_Gold(n) or n % 2 == 0:
		return 2
	elif n % 2 == 1:
		return 3
	
print(main())
