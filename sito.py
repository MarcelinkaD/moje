import math
from sys import stdin
input = stdin.readline

def main():
	MAXN = int(100)
	sito = [True] * MAXN
	sito[1], sito[0] = False, False
	
	for i in range(2, int(math.sqrt(MAXN))):
		if sito[i] == True:
			for j in range(i + i, MAXN, i):
				sito[j] = False
				
				
	print(sito)
	
	
main()
