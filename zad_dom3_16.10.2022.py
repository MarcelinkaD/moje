from sys import stdin
input = stdin.readline

def z_10_na_8(n):
	wynik = ""
	while(n > 0):
		if n % 8 == 0:
			wynik += "0"
		elif n % 8 == 1: 
			wynik += "1"
		elif n % 8 == 2:
			wynik += "2"
		elif n % 8 == 3:
			wynik += "3"
		elif n % 8 == 4:
			wynik += "4"
		elif n % 8 == 5:
			wynik += "5"
		elif n % 8 == 6: 
			wynik += "6"
		else:
			wynik += "7"
			
		wynik //= 8
	return wynik[::-1]
