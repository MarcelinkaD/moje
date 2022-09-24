from sys import stdin
input = stdin.readline

def main():
	lwie, lkol = map(int, input().split())
	lista = []
	max = -1
	
	for i in range(lwie):
		wiersz = list(map(int, input().split()))
		lista.append(wiersz)
		
	for wiersz in range(lwie):
		if sum(lista[wiersz]) > max:
			max = sum(lista[wiersz])
			
	print(max)
	
main()
