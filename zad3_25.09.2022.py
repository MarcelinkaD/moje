from sys import stdin
input = stdin.readline

def main():
	lwie, lkol = map(int, input().split())
	lista = []
	w = 0
	
	for k in range(lwie):
		wiersz = list(map(int, input().split()))
		lista.append(wiersz)
	
	w += (sum(lista[0]) - lista[0][0]) - lista[0][lkol - 1]
	w += (sum(lista[lwie - 1]) - lista[lwie - 1][0]) - lista[lwie - 1][lkol - 1]

	for i in range(lwie):
		w += lista[i][0]
		w += lista[i][lkol - 1]
		
	print(w)
	
	
main()
