import queue
from sys import stdin
input = stdin.readline

def BFS(od, lw, odl, graf):
	for i in range(1, lw + 1):
		odl[i] = lw + 1
		
	odl[od] = 0
	
	nieod = queue.Queue()
	nieod.put(od)
	while not nieod.empty():
		u = nieod.get()
		for somsiad in graf[u]:
			if odl[u] + 1 < odl[somsiad]:
				odl[somsiad]  = odl[u] + 1
				nieod.put(somsiad)
				

def main():
	lw, lk = map(int, input().split())
	graf = [[] for _ in range(lw + 1)]
	odl = [0 for i in range(lw + 1)]
	
	for _ in range(lk):
		od, do = map(int, input().split())
		graf[od].append(do)
		graf[do].append(od)
		
	a, b, c = map(int, input().split())
	
	BFS(a, lw, 	odl, graf)
	
	adob = odl[b]
	# ~ breakpoint()
	BFS(c, lw, odl, graf)
	
	cdoa = odl[a]
	cdob = odl[b]
	
	if adob == cdoa + cdob:
		print("TAK")
	else:
		print("NIE")
	
main()
