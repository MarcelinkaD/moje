import math
from sys import stdin
input = stdin.readline
tablica = []

def generowanie_licz(liczba, pozostale):
	if len(liczba) > 0:
		tablica.append(int(liczba))
	for i in range(len(pozostale)):
		temp = list(pozostale)
		del temp[i]
		generowanie_licz(liczba + str(pozostale[i]), temp)

def main():
	n = str(input().strip())
	max_wyn = 0
	generowanie_licz("", list(n))
	wyn = "NIE"
	tablica.sort(reverse = True)
	# ~ breakpoint()
	for i in tablica:
		if math.sqrt(i) > int(math.sqrt(i)):
			continue
		else:
			wyn = int(i)
			break
	print(wyn)
			
	
main()
