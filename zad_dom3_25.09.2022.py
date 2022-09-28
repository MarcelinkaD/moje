from sys import stdin
input = stdin.readline

def main():
	lwie, lkol = map(int, input().split())
	lista = []
	maxi = -1
	
	for i in range(lwie):
		wiersz = list(map(int, input().split()))
		maxi = max(max(wiersz), maxi)
		lista.append(wiersz)
		
	for i in range(lwie):
		for k in range(lkol):
			if lista[i][k] == maxi:
				lista[i][k] = "?"
				
				
	for i in lista:
		kw = ""
		for k in i:
			kw += str(k) + " "
			
		print(kw)
	
	
main()
