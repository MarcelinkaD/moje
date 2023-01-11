import random
from sys import stdin
input = stdin.readline

def main():
	odp = {16 : "województwa", 18 : "stolice województw", 380 : "powiaty", 4 : "powiato - miasta w wielkopolsce", 2477 : "gminy", 1513 : "gminy wiejskie", 302 : "gminy miejskie", 662 : "gminy miejsko - wiejskie"}
	liczby = [16, 18, 380, 4, 2477, 1513, 302, 662]
	
	while len(liczby) > 0:
		l = liczby[random.randint(0, len(liczby) - 1)]
		print(l)
		w = str(input().strip())
		
		if w == odp[l]:
			print("brawo")
			print("\n")
		else:
			print("źle")
			print("poprawna odp ===> " + odp[l])
			print("\n")
			
		liczby.remove(l)
	
main()
