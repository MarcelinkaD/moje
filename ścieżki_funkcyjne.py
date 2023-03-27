import math
from sys import setrecursionlimit
setrecursionlimit(1000000)

from sys import stdin
input = stdin.readline

def dfs(odw, akt_sciezka, sciezki, wierz, graf):    
	if wierz not in odw:
		akt_sciezka.append(wierz)
		odw.add(wierz)              
		for sasiad in graf[wierz]:
			dfs(odw, akt_sciezka, sciezki, sasiad, graf)
		akt_sciezka.pop()
	else:
		sciezki.append(akt_sciezka[:])

def znajdz_sciezki(wierzch, graf):
	odw = set()
	sciezki = [[wierzch]]    
	dfs(odw, [], sciezki, wierzch, graf)
	return sciezki

def suma_sciezki(sciezka, wagi):
	suma = 0
	for i in range(1, len(sciezka) + 1):
		suma += math.fmod(wagi[sciezka[i - 1]] * ((-1) ** (i + 1)), (10 ** 9 + 7))
	return suma

def main():
	n = int(input())
	wagi = list(map(int, input().split()))
	wagi.insert(0,0)
	graf = [set() for i in range(n + 1)]

	for para in range(n - 1):
		ten_pierwszy, ten_drugi = map(int, input().split())
		graf[ten_pierwszy].add(ten_drugi)
		graf[ten_drugi].add(ten_pierwszy)
		
	wynik = 0
	for wierz in range(1,n + 1):
		sciezki = znajdz_sciezki(wierz, graf)
		for sciezka in sciezki:
			wynik += math.fmod(suma_sciezki(sciezka,wagi), (10**9 + 7))
		
	print(int(math.fmod(wynik, (10**9 + 7))))
	 
main()
