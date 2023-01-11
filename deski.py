from itertools import accumulate
from sys import stdin
input = stdin.readline

def funkcja(gwo, ile, len_pref, deski):
	pref = [0] * (len_pref + 1)
	for i in range(ile):
		pref[gwo[i]] = 1
		
	nowy_pref = [0] * (len_pref + 1)
	
	for i in range(1, len_pref + 1):
		nowy_pref[i] = nowy_pref[i - 1] + pref[i]
	
	
	for i in range(len(deski)):
		if nowy_pref[deski[i][1]] - nowy_pref[deski[i][0] - 1] == 0:
			return False
			
	return True
	
	

def binary(gwo, len_pref, deski):
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
	
main()
