# https://collabedit.com/ufwn9

import queue as q
from sys import stdin
input = stdin.readline

def BFS(graf, od):
    odl = [n + 1 for _ in range(n + 1)]
    nieod = q.Queue()
    odl[od] = 0
    nieod.add(od)
    
    while not nieod.empty():
        u = nieod.get()
        for sasiad in graf[u]:
            if odl[u] + 1 <= odl[sasiad]:
                odl[sasiad] = odl[u] + 1
                nieod.add(sasiad)
                
    return odl

def main():
    n, k, j, m = map(int, input().split())
    graf = [[] for _ in range(n + 1)]
    w = 1e18
    
    for _ in range(k):
        a, b = map(int, input().split())
        graf[a].append(b)
        
    for wie in range(1, n + 1):
        odl = BFS(graf, wie)
        w = min(w, max(odl[j], odl[m]))
    
    print(w)

    
main()