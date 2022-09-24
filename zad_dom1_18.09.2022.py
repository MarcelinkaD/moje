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
	for i in range(lwie):
		for k in range(lkol):
			# ~ breakpoint()
			w += sum(lista[i]) - lista[i][k]
			
			for c in range(lwie):
				w += lista[c][k]
				
			if w > max:
				max = w
			w = 0
			
				
	print(max)
	
main()
