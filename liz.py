from sys import stdin
input = stdin.readline

def main():
	liczba_czesci = int(input())
	smaki_lizaka = list(map(int, input().split()))
	lewo = [-1e18] * liczba_czesci
	prawo = [1e18] * liczba_czesci
	ostatni = {}
	w = 1e10
	
	for i in range(liczba_czesci):
		if smaki_lizaka[i] in ostatni:
			lewo[i] = ostatni[smaki_lizaka[i]]
		
		ostatni[smaki_lizaka[i]] = i
			
	ostatni = {}
	
	for i in range(liczba_czesci - 1, -1 , -1):
		if smaki_lizaka[i] in ostatni:
			prawo[i] = ostatni[smaki_lizaka[i]]
		
		ostatni[smaki_lizaka[i]] = i

	for i in range(liczba_czesci):
		if prawo[i] == 1e18 and lewo[i] == -1e18:
			continue
		else:
			w = min(w, prawo[i] - lewo[i] + 1)

	w = int(w)
	if w == 1e10 or w > 1e9:
		print("NIE")
	else:
		print(w)
	
main()




