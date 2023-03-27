import bisect as bis
from sys import stdin
input = stdin.readline

def brut(n, l, k):
	l.sort()
	w = 0
	for i in range(n - 1, -1, -1):
		k -= l[i]
		w += 1
		if k <= 0:
			return w
			break
			
def fast(n, l, k):
	l.sort(reverse = True)
	pref = [0] * n
	pref[0] = l[0]
	
	for i in range(1, n):
		pref[i] = pref[i - 1] + l[i]
		
	if n == 1:
		return 1
	else:
		g = bis.bisect_left(pref, k)
		return g + 1
	

import random as ra
licz = 1

while True:
	n = ra.randint(1, 100)
	l = []
	suma = 0

	for _ in range(n):
		c = ra.randint(1, 100)
		l.append(c)
		suma += c
		
	k = ra.randint(1, suma)

	w1, w2 = brut(n, l, k), fast(n, l, k)

	if w1 == w2:
		print("Test " + str(licz) + " " + "OK")
	else:
		print("Test " + str(licz) + " " + "ŹLE")
		print("\n")
		print(n)
		
		for i in l:
			print(i, end = " ")
			
		print("\n")
			
		print(k)
		
		print("Wynik bruta: " + str(w1))
		print("Wynik fasta: " + str(w2))
		
		break
	
	licz += 1
	
