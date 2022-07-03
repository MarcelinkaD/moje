from sys import stdin
from dataclasses import dataclass
input = stdin.readline

@dataclass
class Punkt:
	liczba : int
	czy_pocz : int
	
def main():
	n = int(input())
	punkty = []
	
	# czy_pocz = -1  tzn ze to JEST poczatek
	# czy_pocz = 1  tzn ze to JEST koniec
	
	for k in range(n):
		od, do = map(int, input().split())
		punkty.append(Punkt(od, -1))
		punkty.append(Punkt(do, 1))
		
	punkty.sort(key = lambda punkt: (punkt.liczba, punkt.czy_pocz))
	licz_pkt = len(punkty)
	licznik = 0
	maksik = -1
	
	for p in punkty:
		if p.czy_pocz == -1:
			licznik += 1
		else:
			licznik -= 1
		
		if licznik > maksik:
			maksik = licznik
			
	print(maksik)


main()
