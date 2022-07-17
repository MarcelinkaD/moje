from sys import stdin
input = stdin.readline
import math

def czy_pierwsza(n, sito):
	if sito[n] == True:
		return True
	else:
		return False

def suma(n, sito):
	sr = str(n)
	wk = 0
	for i in sr:
		wk += int(i)
	
	return czy_pierwsza(wk, sito)


def main():
	MAXN = int(1e6 + 3)
	sito = [True] * MAXN
	sito[1] = False

	for i in range(2, MAXN):
		if sito[i] == True:
			for k in range(i * i, MAXN, i):
				sito[k] = False
	
	a, b = map(int, input().split())
	w = 0
	# ~ breakpoint()
	for i in range(a, b + 1):
		if czy_pierwsza(i, sito) == True and suma(bin(i)[2:], sito) == True and suma(i, sito) == True:
			w += 1
	
	return w
			
	
print(main())
