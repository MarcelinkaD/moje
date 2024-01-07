# https://sio2.mimuw.edu.pl/c/zwo20/p/drz/

import queue as q
from sys import stdin
input = stdin.readline

def BFS(graf, n, od, odw, rodzic):
    kol = q.Queue()
    kol.put(od)
    
    while not kol.empty():
        u = kol.get()
        for somsiad in graf[u]:
            if not odw[somsiad]:
                kol.put(somsiad)
                rodzic[somsiad] = u
            elif rodzic[u] != somsiad:
                return "niedrzewo"
        odw[u] = True
            
    for i in range(1, n + 1):
        if not odw[i]:
            return "niedrzewo"
    
    return "drzewo"

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("niedrzewo")
        return

    graf = [[] for _ in range(n + 1)]
    odw = [False for _ in range(n + 1)]
    rodzic = [0 for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graf[a].append(b)
        graf[b].append(a)
        
    akt_w = BFS(graf, n, 1, odw, rodzic)
    
    print(akt_w)
    
main()
