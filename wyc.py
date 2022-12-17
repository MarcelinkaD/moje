from sys import stdin
from dataclasses import dataclass
input = stdin.readline

@dataclass
class Suma:
	wartosc: int
	pozycja: int

def binary(tab, p, liczba):
	k = len(tab)
	while p < k:
		srodek = (k + p) // 2
		if(liczba < tab[srodek].wartosc):
			p = srodek + 1
		else:
			k = srodek
			
	if p == len(tab):
		return -1
	                                                                                                        
	return p

def main():
	n, k = map(int, input().split())
	l = list(map(int, input().split()))

	pref = [Suma(0, 0) for i in range(n)]
	
	for i in range(n):
		pref[i].wartosc = pref[i - 1].wartosc + l[i]
		pref[i].pozycja = i + 1
	
	pref.sort(key = lambda x: -x.wartosc)
	w = -1
	#breakpoint()
	for i in range(n):
		g = binary(pref, i + 1, pref[i].wartosc - k)
		if g != -1 :
			w = max(w,abs(pref[g].pozycja - pref[i].pozycja))			
			
	if w == -1:
		print("BRAK")
	else:
		print(w)
		

			
main()
