# algorytmika - 15.05.2023

from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline

def Dijkstra(graf, od, n):
    odl = [1e18 for _ in range(n + 1)]
    odl[od] = 0
    kol = []
    heapify(kol)
    heappush(kol, (0, od))
    
    while len(kol) != 0:
        w, v = heappop(kol)
        
        if w > odl[v]:
            continue
        
        for sasiad, kr in graf[v]:
            n_odl = w + kr
      
            if (odl[sasiad] <= n_odl):
                continue
          
            odl[sasiad] = n_odl
            heappush(kol, (n_odl, sasiad))
            
    return odl

def main():
    n, k, p = map(int, input().split())
    piz = list(map(int, input().split()))
    graf = [[] for _ in range(n + 1)]
    
    for _ in range(k):
        a, b, w = map(int, input().split())
        graf[a].append((b, w))
        graf[b].append((a, w))
    
    w = [1e18 for _ in range(n + 1)]
    
    for pizza in piz:
        odl = Dijkstra(graf, pizza, n)
        for i in range(1, n + 1):
            w[i] = min(w[i], odl[i])
            
    for i in range(1, n + 1):
        print(w[i], end = " ")
    
main()