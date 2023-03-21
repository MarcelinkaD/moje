import queue
from sys import stdin
input = stdin.readline

def BFS(v, n, odleglosc, graf):
	for i in range(1, n + 1):
		odleglosc[i] = n + 1
	odleglosc[v] = 0
	
	nieodwiedzone = queue.Queue()
	nieodwiedzone.put(v)
	while not nieodwiedzone.empty():
		u = nieodwiedzone.get()
		
		for sasiad in graf[u]:
			if odleglosc[u] + 1 < odleglosc[sasiad]:
				odleglosc[sasiad] = odleglosc[u] + 1
				nieodwiedzone.put(sasiad)


def main():
	lw, lk = map(int, input().split())
	a, b = map(int, input().split())
	graf = [[] for _ in range(lw + 1)]
	odleglosc = [0 for i in range(lw + 1)]
	
	for i in range(lk):
		p, q = map(int, input().split())
		graf[p].append(q)
		
	BFS(a, lw, odleglosc, graf)
	
	if odleglosc[b] == lw + 1:
		print("niestety")
	else:
		print(odleglosc[b])
	
main()
