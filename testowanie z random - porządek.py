def brut(n, l, od, do):
	od -= 1
	w = 0
	ost_wyn = 0
	
	for i in range(od, do):
		if l[i] == "R":
			w += 1
		else:
			ost_wyn += w
			
	
	return ost_wyn

def fast(n, l, od, do):
	liczba_kwiatow = n
	kwiaty = l
	kwiaty = " " + kwiaty
	sumy_pref_R = [0] * (liczba_kwiatow + 7)
	sumy_pref_N = [0] * (liczba_kwiatow + 7)
	sumy_pref_pary_R_przed_N = [0] * (liczba_kwiatow + 7)

	for i in range(1, liczba_kwiatow + 1):
		sumy_pref_N[i] = sumy_pref_N[i - 1]
		if(kwiaty[i] == 'N'):
			sumy_pref_N[i] += 1

	for i in range(1, liczba_kwiatow + 1):
		sumy_pref_R[i] = sumy_pref_R[i - 1]
		if(kwiaty[i] == 'R'):
		   sumy_pref_R[i] += 1
			
	for i in range(1, liczba_kwiatow + 1):
		sumy_pref_pary_R_przed_N[i] = sumy_pref_pary_R_przed_N[i - 1]
		if kwiaty[i] == "N":
			sumy_pref_pary_R_przed_N[i] = sumy_pref_pary_R_przed_N[i] + sumy_pref_R[i]

	a, b = od, do
	index_a = a
	index_b = b
	wynik = 0
	ile_par = sumy_pref_R[index_a - 1] * (sumy_pref_N[index_b] - sumy_pref_N[index_a - 1])
	wynik = sumy_pref_pary_R_przed_N[index_b] - sumy_pref_pary_R_przed_N[index_a - 1] - ile_par
	return wynik

import random

numer_testu = 1
while True:
	n = random.randint(2, 10**4 ) #dla większych liczb strasznie muliło
	a = ""
	for i in range(n):
		co = random.randint(1, 2)
		if co == 1:
			a += "N"
		else:
			a += "R"
			
	o1 = random.randint(1, n - 1)
	o2 = random.randint(o1 + 1, n)
	
	if o1 == o2:
		continue
	
	[wynik1, wynik2] = [brut(n, a, o1, o2), fast(n, a, o1, o2)]
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
