from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	n, m = map(int, input().split())
	ile_czego = list(map(int, input().split()))
	jakie_kolory = list(map(int, input().split()))
	lancuch = list(map(int, input().split()))
	suma = sum(ile_czego)
	glowa = suma - 1 
	ogon = 0
	akt_dlugosc = 0
	wyn = 0
	problem = 0

	if suma > n or n < m:
		print(0)
		return 0
	
	licznik = {}
	for i in range(m):
		licznik[jakie_kolory[i]] = ile_czego[i]

	
	while glowa < n - 1:
		c = C(lancuch[ogon : glowa + 1])
		if c == licznik:
			wyn += 1
		
		glowa += 1
		ogon += 1
		
	c = C(lancuch[ogon : glowa + 1])
		
	if c == licznik:
		
		wyn += 1
	
	print(wyn)

main()
