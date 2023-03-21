# https://szkopul.edu.pl/c/testowy_dd/p/gru/18867/s

from sys import stdin
input = stdin.readline

def fast(n, l):
	wg, wj = 0, 0
	wg2, wj2 = 0, 0
	git1 = 0
	git2 = 0
	git3 = 0
	git4 = 0
	
	for i in range(n):
		if l[i] == 0 and git1 != 1:
			wg = i
			git1 = 1
		
		if l[i] == 1 and git2 != 1:
			wj2 = i
			git2 = 1
			
		if git1 + git2 == 2:
			break

	for i in range(n - 1, -1, -1):
		if l[i] == 1 and git3 != 1:
			wj = i
			git3 = 1
		
		if l[i] == 0 and git4 != 1:
			wg2 = i
			git4 = 1
			
		if git4 + git3 == 2:
			break
		
	
	w1 = wj - wg
	w2 = wg2 - wj2
	w3 = wg2 - wj
	w4 = wj2 - wg
	
	
	return max(max(w1, w2), max(w3, w4))
	
	
def brut(n, l):
	w = 0
	
	for i in range(n):
		for k in range(i, n):
			if l[k] != l[i] and k - i > w:
				w = k - i
				
	return w
	
licznik = 1
import random

while True:
	n = random.randint(1, 100)
	l = []
	
	for _ in range(n):
		l.append(random.randint(0, 1))
		
	if sum(l) == n or sum(l) == 0:
		continue
	
	wyn1, wyn2 = fast(n, l), brut(n, l)
	
	if wyn1 == wyn2:
		print(licznik, "Test:", "OK")
	else:
		print(licznik, "Test:", ":-(")
		print("Wynik bruta:", wyn2)
		print("Wynik fasta:", wyn1)
		print(n)
		
		for i in l:
			print(i, end = " ")
			
		break
		
	licznik += 1
		
		
		
	
	
	
	
