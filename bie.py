from sys import stdin
input = stdin.readline

def main():
	liczba_liczb = int(input())
	liczby = []
	
	for i in range(liczba_liczb):
		k = int(input())
		liczby.append(k)
	
	liczby.sort()
	
	glowa = 2
	ogon = 0
	naj_wynik = 0
	# ~ breakpoint()
	while glowa < liczba_liczb:
		pierwsze = liczby[ogon]
		drugie = liczby[ogon + 1]
		if pierwsze + drugie > liczby[glowa]:
			wynik = (glowa - ogon) + 1
			if wynik > naj_wynik:
				naj_wynik = wynik
			glowa += 1
		else:
			ogon += 1
	
	print(naj_wynik)
			
	
main()
