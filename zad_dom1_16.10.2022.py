from sys import stdin
input = stdin.readline

def z_10_na_3(n):
	wynik = ""
	while(n > 0):
		if(n % 3 == 0):
			wynik += "0"
		elif(n % 3 == 1): 
			wynik += "1"
		else:
			wynik += "2"
		wynik //= 3
	return wynik[::-1]
