import math
from sys import stdin
input = stdin.readline

def main():
	MAXN = int(1e6+4)
	sito = [0, 1] * (MAXN//2) + [1]
	sito[1], sito[2] = 0, 1
		
	for i in range(3, int(MAXN**0.5+1), 2):
		if sito[i] == 1:
			sito[i*i::2*i] = [0] * int((MAXN+2*i-1-i*i)/(2*i))
	
	n = int(input())
	d = 2
	
	if n == 0 or n == 1:
		print(n)
		return 0
	# ~ breakpoint()
	while d * d <= n:
		temp = 0
		while n % d == 0 and sito[d] == 1:
			if temp == 0:
				print(d)
			n //= d
			temp = 1
			
		d += 1
			
	if n > 1:
		print(n)
	
	
main()
