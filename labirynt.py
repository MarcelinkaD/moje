# https://cses.fi/problemset/task/1193

import queue as q
from sys import stdin
input = stdin.readline

def inRange(x, y, n, m):
    if x < n and y < m:
        if 0 <= x and 0 <= y:
            return True
    
    return False

def BFS(x, y, graf, koniec, m, n):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = []
    czyodw = set()
    queue.append([(x, y)])
    while queue:
        sciezka = queue.pop(0)
        wie = sciezka[-1]

        if wie == koniec:
            return sciezka

        for sasiad in graf[wie[0]][wie[1]]:
            if not visited[sasiad[0]][sasiad[1]]:
                visited[sasiad[0]][sasiad[1]] = True
                nowa_scie = list(sciezka)
                nowa_scie.append(sasiad)
                queue.append(nowa_scie)
        
    return "NO"      
            

def main():
    n, m = map(int, input().split())
    lab = []
    droga = ""
    
    for _ in range(n):
        lab.append(str(input().strip()))
        
    graf = [[[] for _ in range(m)] for _ in range(n)]    
    ruchy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == "." or lab[i][j] == "B" or lab[i][j] == "A":
                for ruch in ruchy:
                    nx, ny = i + ruch[0], j + ruch[1]
                    if inRange(nx, ny, n, m) and (lab[nx][ny] == "." or lab[nx][ny] == "B" or lab[nx][ny] == "A"):
                        graf[i][j].append((nx, ny))
                        
            if lab[i][j] == "A":
                sx, sy = i, j
            
            if lab[i][j] == "B":
                kx, ky = i, j
    
    if len(graf[sx][sy]) == 0 or len(graf[kx][ky]) == 0:
        print("NO")
        return
    
    sciezka = BFS(sx, sy, graf, (kx, ky), m, n)
    if sciezka == "NO":
        print("NO")
        return
    print("YES")
    print(len(sciezka) - 1)
    sc = ""
    poprzedni = sciezka[0]
    
    for i in range(1, len(sciezka)):
        sasiad = sciezka[i]
        if poprzedni[0] < sasiad[0]:
            sc += "D"
        elif poprzedni[0] > sasiad[0]:
            sc += "U"
        elif poprzedni[1] < sasiad[1]:
            sc += "R"
        else:
            sc += "L"
        
        poprzedni = sasiad
    print(sc)


main()    