from itertools import accumulate
from sys import stdin
input = stdin.readline

def funkcja(gwo, ile, len_pref, deski):
	pref = [0] * (len_pref + 1)

	for i in range(ile):
		pref[gwo[i]] = 1
		
	pref = list(accumulate(pref))
	
	for i in range(len(deski)):
		if pref[deski[i][1]] - pref[deski[i][0] - 1] == 0:
			return False
			
	return True
	
	

def binary(gwo, len_pref, deski):
	# ~ breakpoint()
	pocz = 1 
	kon = len(gwo)
	while pocz < kon:
		sro = (kon + pocz) // 2
		if funkcja(gwo, sro, len_pref, deski):
			kon = sro
		else:
			pocz = sro + 1
			
	return pocz

def main():
	n, k = map(int, input().split())
	deski = []
	maxi = 0
	
	for _ in range(n):
		a, b = map(int, input().split())
		deski.append((a, b))
		maxi = max(maxi, b)
	
	gwozdzie = list(map(int, input().split()))
	
	print(binary(gwozdzie, maxi, deski))
	
	# ~ breakpoint()
	
main()
