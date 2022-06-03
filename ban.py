from sys import stdin
input = stdin.readline

def main(args):
	liczba_gosci = int(input())
	lista_gosci = [0]
	ci_co_byli = []
	wynik = 0
	l1 = 1
	l2 = 1 
	
	for i in range(liczba_gosci):
		k = int(input())
		lista_gosci.append(k)
	
	while len(ci_co_byli) != len(lista_gosci) and l2 <= liczba_gosci:
		na_lewo = lista_gosci[l1]
		l1 = l2
		sprawdzam = False
		
		while na_lewo not in ci_co_byli:
			ci_co_byli.append(na_lewo)
			l1 = na_lewo
			na_lewo = lista_gosci[l1]
			sprawdzam = True
				
		if sprawdzam:
			wynik += 1
			
		l2 += 1

		
	print(wynik)

		
		

if __name__ == '__main__':
    import sys
    main(sys.argv)
		
