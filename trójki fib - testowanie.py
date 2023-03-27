from sys import stdin
input = stdin.readline

def czy_fib(licz):
	if licz == 0 or licz == 1:
		return True
	l1, l2 = 0, 1
	while l1 + l2 < licz:
		suma = l1 + l2 
		l1 = l2
		l2 = suma
		
	if l1 + l2 == licz:
		return True
	else:
		return False

def fast(n, l):
	w = 0

	for i in l:
		if czy_fib(i) == False:
			l.remove(i)
			
	for i in range(len(l)):
		for j in range(i + 1, len(l)):
			for k in range(j + 1, len(l)):
				if l[i] < l[j] < l[k]:
					w += 1
	
	return w
	
def slow(n, l):
	w = 0
	
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1, n):
				if l[i] < l[j] < l[k]:
					if czy_fib(l[i]) and czy_fib(l[j]) and czy_fib(l[k]):
						w += 1
						
	return w

licznik = 1
import random as rd

while True:
	n = rd.randint(1, 20)
	s = []
	# ~ breakpoint()
	for _ in range(n):
		s.append(rd.randint(0, 13))

	wynik2 = slow(n, s)
	wynik1 = fast(n, s)


	if wynik1 == wynik2:
		print("Test", licznik, "OK")
	else:
		print("Test", licznik, "Źle :(")
		print("\n")
		print("Wynik bruta:", wynik2)
		print("Wynik fasta:", wynik1)
		print("\n")
		print(n)
		print(s)
		break
		
	licznik += 1
