from sys import stdin
input = stdin.readline

def z_10_na_5(n):
	wynik = ""
	while(n > 0):
		if(n % 5 == 0):
			wynik += "0"
		elif(n % 5 == 1): 
			wynik += "1"
		elif(n % 5 == 2):
			wynik += "2"
		elif(n % 5 == 3):
			wynik += "3"
		else:
			wynik += "4"
			
		wynik //= 5
	return wynik[::-1]
