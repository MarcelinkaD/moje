from sys import stdin
input = stdin.readline

def main():
	liczba_liczb = int(input())
	liczby = []
	
	for i in range(liczba_liczb):
		k = int(input())
		liczby.append(k)
	
	liczby.sort()
	glowa = 1
	ogon = 0
	akt_wyn = 1
	max_wyn = -1
	while ogon < liczba_liczb:
		while glowa < liczba_liczb and liczby[ogon] + liczby[ogon + 1] > liczby[glowa]:
			glowa += 1
			akt_wyn += 1
			max_wyn = max(max_wyn, akt_wyn)
			
		ogon += 1
		akt_wyn -= 1
		
	print(max_wyn)
	
main()
