from sys import stdin
input = stdin.readline

def z_10_na_16(n):
	w = ""
	while n > 0:
		k = liczba % 16
		if k < 10:
			w += str(liczba % 16)
		else:
			if k == 10:
				w += "A"
			if k == 11:
				w += "B"
			if k == 12:
				w += "C"
			if k == 13:
				w += "D"
			if k == 14:
				w += "E"
			if k == 15:
				w += "F"
			
		w //= 16
	return w[::-1]

