import random

numer_testu = 1
while True:
	n = random.randint(1, 10)
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = random.randint(1, 10**9)
	
	[wynik1, wynik2] = [brut(n, a), fast(n, a)]
	if wynik1 == wynik2:
		print("Test " + str(numer_testu) + "     OK")
	else:
		print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
		print("\nwejscie:")
		print(n)
		for i in range(n):
			print(a[i], end = ' ')
		print("\n\nwynik bruta:         " + str(wynik1))
		print("\nwynik wzorcowki:     " + str(wynik2))
		
		break
	
	numer_testu += 1
