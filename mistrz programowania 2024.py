from dataclasses import dataclass
from sys import stdin
input = stdin.readline

@dataclass
class Uczestnik:
	liczba_rund : int
	ile_max : int
	suma_pkt : int
	nazwa : str
	r1 : int
	r2 : int
	r3 : int
	r4 : int
	r5 : int
	miejsce: int

def order(x):
	return (-x.liczba_rund, -x.ile_max, -x.suma_pkt, x.nazwa)

def main():
	n = int(input())
	l = []
	
	for _ in range(n):
		tab = list(map(str, input().split()))
		liczb_rund = 0
		suma = 0
		ile_max = 0
		
		for i in range(1, len(tab)):
			if int(tab[i]) == 500:
				ile_max += 1
			if int(tab[i]) != 0:
				suma += int(tab[i])
				liczb_rund += 1
			
		l.append(Uczestnik(liczb_rund, ile_max, suma, tab[0], int(tab[1]), int(tab[2]), int(tab[3]), int(tab[4]), int(tab[5]), 0))
				
	l = sorted(l, key = lambda j: order(j))
	
	miejsce = 1
	ost_wyn = (float('inf'), float('inf'), float('inf'))

	for i, uczestnik in enumerate(l):
		if (uczestnik.liczba_rund, uczestnik.ile_max, uczestnik.suma_pkt) != ost_wyn:
			miejsce = i + 1
			ost_wyn = (uczestnik.liczba_rund, uczestnik.ile_max, uczestnik.suma_pkt)
		uczestnik.miejsce = miejsce

	for uczestnik in l:
		print(f"{uczestnik.miejsce} {uczestnik.nazwa} {uczestnik.suma_pkt} {uczestnik.r1} {uczestnik.r2} {uczestnik.r3} {uczestnik.r4} {uczestnik.r5}")
	
main()
