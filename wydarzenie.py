# https://szkopul.edu.pl/problemset/problem/yXGsRXacUJsq6aLwOx4VOIQ1/site/?key=statement

from queue import Queue as Q
from sys import stdin
input = stdin.readline

def BFS(od, graf, n):
    odw = [False for _  in range(n + 1)]
    kol = Q()
    kol.put(od)
    
    while not kol.empty():
        u = kol.get()
        for sasiad in graf[u]:
            if odw[sasiad] == False:
                odw[sasiad] = True
                kol.put(sasiad)
        
        if len(graf[u]) == 0:
            return u

def main():
    n = int(input())
    osoby = list(map(int, input().split()))
    m = int(input())
    od_kogo = list(map(int, input().split()))
    graf = [[] for _ in range(n + 1)]
    byli = set()
    w = 0
    osoby.insert(0, 0)
    
    for i in range(1, n + 1):
        if osoby[i] != 0:
            graf[i].append(osoby[i])
    
    for i in range(m):
        if osoby[od_kogo[i]] == 0:
            if od_kogo[i] not in byli:
                w += 1
                byli.add(od_kogo[i])
        else:
            zrodlo = BFS(od_kogo[i], graf, n)
            
            if zrodlo not in byli:
                w += 1
                byli.add(zrodlo)
    
    print(w)


    
main()