from sys import stdin
input = stdin.readline
import math

def specjalna_funkcja(x, tab, kd):
	suma = 0
	ile_wedkarzy_zostalo = kd - 1
	i = 1
	while i < len(tab) and ile_wedkarzy_zostalo > 0:
		while i < len(tab) and suma < x:
			suma += tab[i]
			i += 1
		if suma >= x:
			ile_wedkarzy_zostalo -= 1
			suma = 0
		
	if ile_wedkarzy_zostalo == 0:
		return True
	else:
		return False
	
def main():
	
	try:
		liczba_stanowisk, liczba_wedkarzy = map(int, input().strip().split())
		stanowiska = list(map(int, input().strip().split()))

	except Exception as e: print(type(e).__name__)

	#print(str(liczba_stanowisk)+"_"+str(liczba_wedkarzy))
	print("_".join(map(str,stanowiska)))
	return

	ostatnie = stanowiska[liczba_stanowisk - 1]
	
	for i in range(1, liczba_stanowisk):
		stanowiska[i] = stanowiska[i] - stanowiska[i - 1]
		
	lewo, prawo = 1, ostatnie
	while lewo < prawo:
		srodek = math.ceil((lewo + prawo + 1) // 2)
		if specjalna_funkcja(srodek, stanowiska, liczba_wedkarzy) == True:
			lewo = srodek
		else:
			prawo = srodek - 1
	
	print(srodek // 2)
	
main()
