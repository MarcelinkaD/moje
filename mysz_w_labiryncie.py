# https://szkopul.edu.pl/problemset/problem/Wm6JcGbhvM2t4Hfam8UuuXLl/site/?key=statement

from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(1000000)

def inRange(y, x, n, m):
    if y < m and x < n:
        if 0 <= x and 0 <= y:
            return True
    
    return False

def DFS(y, x, graf, czy_odw):
    if not czy_odw[y][x]:
        czy_odw[y][x] = True
        for sasiad in graf[y][x]:
            if not czy_odw[sasiad[0]][sasiad[1]]:
                DFS(sasiad[0], sasiad[1], graf, czy_odw)

def main():
    n, m = map(int, input().split())
    graf = [[[] for _ in range(n)] for _ in range(m)]
    l = []
    
    for i in range(m):
        wiersz = str(input().strip())
        l.append(wiersz)
        
    ruchy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    for i in range(m):
        for k in range(n):
            if l[i][k] != "x":
                for ruch in ruchy:
                    ny, nx = i + ruch[0], k + ruch[1]
                    if inRange(ny, nx, n, m) and l[ny][nx] != "x":
                        graf[i][k].append((ny, nx))
                        
            if l[i][k] == "o":
                sy, sx = i, k
            
            if l[i][k] == "w":
                ky, kx = i, k
                
    if len(graf[sy][sx]) == 0 or len(graf[ky][kx]) == 0:
        print("NIE")
        return
    
    czy_odw = [[False for _ in range(n)] for _ in range(m)]
    DFS(sy, sx, graf, czy_odw)
    
    if czy_odw[ky][kx]:
        print("TAK")
    else:
        print("NIE")
    
main()