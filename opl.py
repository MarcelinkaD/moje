from sys import stdin
from collections import Counter
input = stdin.readline

def main():
	a, b = map(int, input().split())
	c, d = map(int, input().split())
	co = Counter([a, b, c, d])
	w = 0
	wys, sze = map(int, input().split())
	obraz = []
	
	if wys == 1:
		return w
	
	for i in range(wys):
		li = list(map(int, input().split()))
		obraz.append(li)

	for linia in range(wys - 1):
		for liczba in range(sze - 1):
			a, b, c, d = obraz[linia][liczba], obraz[linia][liczba + 1], obraz[linia + 1][liczba], obraz[linia + 1][liczba + 1]
			l = Counter([a, b, c, d])
			if l ==  co:
				w += 1
				
				
	return w
	
print(main())
