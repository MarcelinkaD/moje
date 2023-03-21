import queue as q

def BFS(od, n, graf, odl):
	for i in range(1, n + 1):
		odl[i] = n + 1
		
	odl[od] = 0
	
	nieod = q.Queue()
	nieod.put(od)
	while not nieod.empty():
		u = nieod.get()
		for somsiad in graf[u]:
			if odl[u] + 1 < odl[somsiad]:
				odl[somsiad] = odl[u] + 1
				nieod.put(somsiad)
				
odl = [0, 0, 0, 0, 0]
BFS(1, 4, [[], [2, 3], [1], [4], [3]], odl)
print(odl)
