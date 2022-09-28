from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	lista = []
	w = 0
	i = 0
	
	for k in range(n):
		wiersz = list(map(int, input().split()))
		lista.append(wiersz)
		
	while i < n:
		w += lista[i][n - i - 1]
		i += 1
		
	i = 0
	while i < n:
		w += lista[i][i]
		i += 1
		
	print(w - lista[n // 2][n // 2])
	
main()
