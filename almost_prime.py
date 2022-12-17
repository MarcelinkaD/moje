from sys import stdin
input = stdin.readline
import math

def czy_pierwsza(x):
	for c in range(2, int(math.sqrt(x)) + 1):
		if x % c == 0:
			return False
			
	return True

def main():
	n = int(input())
	w = 0

	for liczba_ktora_testujemy in range(1, n + 1):
		dzielniki = []
		for k in range(1, int(math.sqrt(liczba_ktora_testujemy))+1):
			if(liczba_ktora_testujemy % k == 0):
				dzielniki.append(k)
				drugiDzielnik = liczba_ktora_testujemy/k
				if(drugiDzielnik != k):      
					dzielniki.append(int(drugiDzielnik))
	
		dzielniki.sort()
		ile = 0
		for k in dzielniki:
			if k != 1 and czy_pierwsza(k):
				ile += 1
				
		if ile == 2:
			w += 1
		
	print(w)
	
main()
