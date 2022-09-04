import math
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	MAXN = int(1e6 + 6)
	sito = [True] * MAXN
	
	for i in range(2, int(math.sqrt(MAXN))):
		# ~ breakpoint()
		if sito[i] == True:
			for k in range(i + i, int(math.sqrt(MAXN)), i):
				sito[k] = False
		
	j = 2
	
	while n != 0:
		if sito[j] == True:
			print(j)
			n -= 1
		j += 1
	
main()
