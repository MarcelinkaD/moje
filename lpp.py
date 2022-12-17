import math
import bisect
from sys import stdin
input = stdin.readline

def binary(li, n):
	g = bisect.bisect_left(li, n)
	if g != len(li) and li[g] == n:
		return g
	else:
		return -1

def main():
	MAXN = int(1e6+4)
	sito = [0, 1] * (MAXN//2) + [1]
	sito[1], sito[2] = 0, 1
		
	for i in range(3, int(MAXN**0.5+1), 2):
		if sito[i] == 1:
			sito[i*i::2*i] = [0] * int((MAXN+2*i-1-i*i)/(2*i))
			
	prawpie = []

	for i in range(2, len(sito)):
		if sito[i] == 1:
			prawpie.append(i * i)
	
			
	n = int(input())
	l = list(map(int, input().split()))
	
	for i in l:
		if binary(prawpie, i) == -1:
			print("NIE")
		else:
			print("TAK")
	
main()

