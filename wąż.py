# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/waz/24155/

import queue as q
from sys import stdin
input = stdin.readline

def inRange(y, x, n, m):
    if y < n and x < m:
        if 0 <= x and 0 <= y:
            return True
    
    return False

def main():
    n, m, r = map(int, input().split())
    kierunek = str(input().strip())
    jab = [[False for _ in range(m)] for _ in range(n)]
    plansza = []
    
    for _ in range(n):
        linia = str(input().strip())
        plansza.append(linia)
        
    for i in range(n):
        for j in range(m):
            if plansza[i][j] == "W":
                y, x = i, j
            elif plansza[i][j] == "J":
                jab[i][j] = True
        
    waz = [[False for _ in range(m)] for _ in range(n)]
    waz[y][x] = True
    kolejka = q.Queue()
    kolejka.put((y, x))
    kroki = list(map(str, input().split()))
    do_przodu = {"N" : (-1, 0), "W" : (0, -1), "E" : (0, 1), "S" : (1, 0)}
    prawo = {"N" : (0, 1), "W" : (-1, 0), "E" : (1, 0), "S" : (0, -1)}
    lewo = {"N" : (0, -1), "W" : (1, 0), "E" : (-1, 0), "S" : (0, 1)}
    zp = {"N" : "E", "W" : "N", "E" : "S", "S" : "W"}
    zl = {"N" : "W", "W" : "S", "E" : "N", "S" : "E"}
    
    for i in range(r):
        if kroki[i] == "N":
            ny, nx = do_przodu[kierunek]
        elif kroki[i] == "P":
            ny, nx = prawo[kierunek]
            kierunek = zp[kierunek]
        else:
            ny, nx = lewo[kierunek]
            kierunek = zl[kierunek]
        ny += y
        nx += x
    
        if inRange(ny, nx, n, m):
            if waz[ny][nx] == False:
                kolejka.put((ny, nx))
                waz[ny][nx] = True
            else:
                print(i + 1)
                return
            if jab[ny][nx] == False:
                starey, starex = kolejka.get()
                waz[starey][starex] = False
            else:
                jab[ny][nx] = False
            
        else:
            print(i + 1)
            return 
        
        y = ny
        x = nx
            
                
    print("OK")
        
    
main()