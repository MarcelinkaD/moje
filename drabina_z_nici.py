# https://szkopul.edu.pl/c/testowy_dd/p/dra/

import queue
from sys import stdin
input = stdin.readline

def zle():
    print("NIE")
    quit()

def BFS(od, n, graf):
    odl = [n for _ in range(n + 1)]
    kol = queue.Queue()
    kol.put(od)
    odl[od] = 0
    
    while not kol.empty():
        u = kol.get()
        
        for sasiad in graf[u]:
            if odl[u] + 1 < odl[sasiad]:
                odl[sasiad] = odl[u] + 1
                kol.put(sasiad)
    
    return odl

def main():
    n, m = map(int, input().split())
    graf = [[] for _ in range(n + 1)]
    
    if n % 2 == 1:
        zle()
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        graf[a].append(b)
        graf[b].append(a)
        
    krancowe = []
    
    for i in range(1, n + 1):
        if len(graf[i]) == 1:
            krancowe.append(i)
        elif len(graf[i]) == 3:
            continue
        else:
            zle()
            
    if len(krancowe) != 4:
        zle()
    
    odl1 = BFS(krancowe[0], n, graf)
    
    od = krancowe[1]
    for i in [2, 3]:
        if odl1[krancowe[i]] == 3:
            od = krancowe[i]
    
    odl2 = BFS(od, n, graf)
    
    row1 = [0 for _ in range(n // 2)]
    row2 = [0 for _ in range(n // 2)]
    
    for i in range(1, n + 1):
        if odl1[i] < odl2[i]:
            row1[odl1[i]] = i
        elif odl1[i] > odl2[i]:
            row2[odl2[i]] = i
        else:
            zle()

    print("TAK")
    for i in range(n // 2):
        print(row1[i], row2[i])
            
    
main()