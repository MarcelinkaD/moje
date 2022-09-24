from sys import stdin
input = stdin.readline

def dfs(odw, graf, wierz, wyn):  
	if wierz not in odw:
		wyn.add(wierz)
		odw.add(wierz)
		for somsiad in graf[wierz]:
			dfs(odw, graf, somsiad, wyn)
			
	return wyn

def main():
	n, m = map(int, input().split())
	wie = [[] for i in range(n + 1)]
	odw = set()
	wyn = set()
	
	for para in range(m):
		ten_pierwszy, ten_drugi = map(int, input().split())
		wie[ten_pierwszy].append(ten_drugi)
		wie[ten_drugi].append(ten_pierwszy)
	
	wyn = dfs(odw, wie, 1, wyn)
	# ~ breakpoint()
	for i in range(1, n + 1):
		if i in wyn:
			print("TAK")
		else:
			print("NIE")
	
main()
