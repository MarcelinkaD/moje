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
	for i in range(lkol):
		for k in range(lwie):
			w += lista[k][i]
			
		if w > max:
			max = w
		
		w = 0
		
	print(max)
	
main()

