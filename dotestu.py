from heapq import heapify, heappop, heappush
from collections import deque
from collections import Counter as C
from itertools import accumulate
from dataclasses import dataclass
import queue as q
from sys import stdin
input = stdin.readline
import math

def BFS(od, graf , n):
    odl = [1e18 for _ in range(n)]
    kol = q.Queue()
    kol.put(od)
    odl[od] = 0

    while not kol.empty():
        u = kol.get()
        for sasiad in graf[u]:
            if odl[u] + 1 < odl[sasiad[0]]:
                odl[sasiad[0]] = odl[u] + 1
                kol.put(sasiad[0])

    return odl

def Dijkstra(graf, od, k, odl_bfs, n):
    odl = [1e18 for _ in range(n)]
    odl[od] = 0
    kol = []
    heapify(kol)
    heappush(kol, (0, od))
    
    while len(kol) != 0:
        wag, wie = heappop(kol)
        
        if wag > odl[wie] or odl_bfs[wie] > k:
            continue
        
        for sasiad, kraw in graf[wie]:
            now_odl = wag + kraw
            
            if odl[sasiad] <= now_odl:
                continue
            
            odl[sasiad] = now_odl
            heappush(kol, (now_odl, sasiad))

    return odl



def findCheapestPrice(n, loty, od, do, k):
    graf = [[] for _ in range(n)]

    for i in loty:
        graf[i[0]].append((i[1], i[2]))

    odl_bfs = BFS(od, graf, n)
    
    for i in range(n):
        odl_bfs[i] -= 1
    
    if odl_bfs[do] > k:
        return -1

    odl_dij = Dijkstra(graf, od, k, odl_bfs, n)

    if odl_dij[do] == 1e18:
        return -1
    
    return odl_dij[do]


    
print(findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))

