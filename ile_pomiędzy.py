# https://szkopul.edu.pl/problemset/problem/ipo/site/?key=statement

import queue as q
from sys import stdin
input = stdin.readline

def BFS(n, graf, od):
	odl = [0 for _ in range(n + 1)]
	for i in range(1, n + 1):
		odl[i] = n + 1
		
	odl[od] = 0
	nieod = q.Queue()
	nieod.put(od)
	
	while not nieod.empty():
		v = nieod.get()
		for somsiad in graf[v]:
			if odl[v] + 1 <= odl[somsiad]:
				odl[somsiad] = odl[v] + 1
				nieod.put(somsiad)
				
	return odl
	

def main():
	n, k, zrodlo = map(int, input().split())
	graf = [[] for _ in range(n + 1)]
	
	for _ in range(k):
		a, b = map(int, input().split())
		graf[a].append(b)
		graf[b].append(a)
		
	o = BFS(n, graf, zrodlo)
	
	for i in range(1, n + 1):
		if o[i] == n + 1:
			print(-1)
		else:
			print(o[i])
	
main()
