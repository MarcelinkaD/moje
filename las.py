# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/las/18853/

import queue as q
from sys import stdin
input = stdin.readline

def bfs(odw, l, n, od, x, graf):
    wielk = 1
    nieod = q.Queue()
    nieod.put(od)
    while not nieod.empty():
        u = nieod.get()
        for somsiad in graf[u[0]][u[1]]:
            if odw[somsiad[0]][somsiad[1]] == False and l[somsiad[0]][somsiad[1]] <= x:
                wielk += 1
                odw[somsiad[0]][somsiad[1]] = True
                nieod.put(somsiad)
                
    return wielk

def naj_wys(x, l, n, graf):
    naj_wys = -1
    odw = [[False for _  in range(n)] for _ in range(n)]
    
    for i in range(n):
        for k in range(n):
            if odw[i][k] == False:
                naj_wys = max(naj_wys, bfs(odw, l, n, (i, k), x, graf))
                
    return naj_wys
    

def czy_dobrze(x, dom, l, n, graf):
    if naj_wys(x, l, n, graf) <= dom:
        return True
    else:
        return False

def inRange(x, y, n, m):
    return (0 <= x < n and 0 <= y < m)

def main():
    n, dom = map(int, input().split())
    l = []
    mini, maxi = 1e10, -1
    
    for _  in range(n):
        li = list(map(int, input().split()))
        mini = min(mini, min(li))
        maxi = max(maxi, max(li))
        l.append(li)
        
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    graf = [[[] for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for k in range(n):
            for ruch in moves:
                if inRange(ruch[0] + i, ruch[1] + k, n, n):
                    graf[i][k].append((ruch[0] + i, ruch[1] + k))
        
    pocz, kon = mini, maxi
    wynik = 1e10
    
    while pocz < kon:
        sr = (pocz + kon) // 2
        if czy_dobrze(sr, dom, l, n, graf) == False:
            kon = sr
            wynik = min(wynik, sr)
        else:
            pocz = sr + 1
    
    print(wynik)
    
main()