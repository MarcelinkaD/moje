from sys import stdin
input = stdin.readline

def main():
	lwie, lkol = map(int, input().split())
	lista = []
	max = -1
	
	for i in range(lwie):
		wiersz = list(map(int, input().split()))
		lista.append(wiersz)
		
	w = 0
	for wiersz in range(lwie - 1):
		for kolumna in range(lkol - 1):
			# ~ breakpoint()
			w += lista[wiersz][kolumna]
			w += lista[wiersz + 1][kolumna]
			w += lista[wiersz][kolumna + 1]
			w += lista[wiersz + 1][kolumna + 1]
			
			if w > max:
				max = w
			w = 0
		
	print(max)
			
main()
