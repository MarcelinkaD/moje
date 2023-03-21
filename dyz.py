from sys import stdin
input = stdin.readline
from itertools import accumulate

def main():
	MAXN = int(1e7+4)
	sito = [0, 1] * (MAXN//2) + [1]
	sito[1], sito[2] = 0, 1
		
	for i in range(3, int(MAXN**0.5+1), 2):
		if sito[i] == 1:
			sito[i*i::2*i] = [0] * int((MAXN+2*i-1-i*i)/(2*i))
	
	q = int(input())
	pref = list(accumulate(sito))
	
	for k in range(q):
		a, b = map(int, input().split())
		print(pref[b] - pref[a - 1])

main()
