from sys import stdin
import math
input = stdin.readline

def wylicz_wynik(l_z):
	if(l_z == 1 or l_z == 2):
		return 1
	if l_z % 3 == 0:
		return l_z // 3 
	else:
		return (l_z // 3) + 1
		return (l_z // 3) + 1

def main(args):
	liczba_uczniow = int(input())
	krzesla = str(input())
	wynik = 0
	l_z = 0
	
	
	czy_z = False
	#breakpoint()				
	for i in range(0, liczba_uczniow):
		znak = krzesla[i]
		
		if(znak == "Z"):
			l_z += 1
			czy_z = True
		else:
			if(czy_z == True):
				wynik += wylicz_wynik(l_z)
				
			czy_z = False
			l_z = 0
	
	#breakpoint()		
	if(l_z != 0):
		wynik += wylicz_wynik(l_z)
	
	print(wynik)
	
if __name__ == '__main__':
    import sys
    main(sys.argv)
