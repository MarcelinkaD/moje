from sys import stdin
input = stdin.readline

def main():
	lwie, lkol = map(int, input().split())
	lista = []
	wynik = []
	
	for i in range(lwie):
		wiersz = list(map(int, input().split()))
		lista.append(wiersz)
		
		
	w = []
	for i in range(lkol):
		for k in range(lwie):
			w.append(lista[k][i])
		w.reverse()
		wynik.append(w)
		w = []
		
	for i in wynik:
		kw = ""
		for k in i:
			kw += str(k) + " "
			
		print(kw)
	
main()
