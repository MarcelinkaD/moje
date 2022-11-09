#do konca nie dziala, nie do konca wiemy czemu :-(
#https://sio2.staszic.waw.pl/c/algorytmika-od-podstaw-20182019/p/kra/1063/

import bisect
from sys import stdin
input = stdin.readline

def main():
	ldzi, lkra = map(int, input().split())
	dzi = list(map(int, input().split()))
	kra = list(map(int, input().split()))
	ms = 0
	
	for i in range(ldzi - 2, -1, -1):
		if dzi[i] < dzi[i + 1]:
			dzi[i + 1] = dzi[i]
			
	dzi.sort()
	# ~ breakpoint()
	for i in range(lkra):
		ms = bisect.bisect_left(dzi, kra[i])		
		odwrocony_ms = len(dzi) - ms - 1
		if i == lkra - 1:
			print(odwrocony_ms + 1)
		dzi = dzi[ms + 1 : len(dzi)]
	
main()

