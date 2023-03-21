import queue
from sys import stdin
input = stdin.readline

def DFS(v, b, odwiedzony, akt_odl):
	odwiedzony[v] = True
	for sasiad in graf[v]:
		if odwiedzony[sasiad] == False:
			DFS(sasiad)



def main():
	lw, lk = map(int, input().split())
	a, b = map(int, input().split())
	graf = [[] for _ in range(lw + 1)]
	odwiedzony = [False for i in range(lw + 1)]

	
	for i in range(lk):
		p, q = map(int, input().split())
		graf[p].append(q)
		
	DFS(a, b, odzwiedzony, 0)
	
	if odleglosc[b] == lw + 1:
		print("niestety")
	else:
		print(odleglosc[b])
	
main()

