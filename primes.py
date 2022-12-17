from sys import stdin
input = stdin.readline
import math

def czy_pierwsza(x):
	if x == 1:
		return False
		
	for c in range(2, int(math.sqrt(x)) + 1):
		if x % c == 0:
			return False
			
	return True

def main():
	n = int(input())
	
	for i in range(1, n):
		if czy_pierwsza(i):
			drugie = n - i
			if czy_pierwsza(drugie):
				print(i, end = " ")
				print(drugie)
				return 0
	
	print(-1)
	
main()
