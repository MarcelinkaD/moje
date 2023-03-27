# algorytmika 19.03.2023

from sys import stdin
input = stdin.readline
import queue as q

def BFS(graf, od, n):
    odl = [n + 1 for _ in range(n + 1)]
    odl[od] = 0
    nieod = q.Queue()
    nieod.put(od)
    
    while not nieod.empty():
        u = nieod.get()
        for sasiad in graf[u]:
            if odl[u] + 1 <= odl[sasiad]:
                odl[sasiad] = odl[u] + 1
                nieod.put(sasiad)
                
    return odl

def main():
    n, k, lp = map(int, input().split())
    graf = [[] for _ in range(n + 1)]
    pizzerie = list(map(int, input().split()))
    w = [1e18 for _ in range(n + 1)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graf[a].append(b)
        
    for pizza in pizzerie:
        odl = BFS(graf, pizza, n)
        for i in range(n + 1):
            w[i] = min(w[i], odl[i])
            
    print(w)
    
main()