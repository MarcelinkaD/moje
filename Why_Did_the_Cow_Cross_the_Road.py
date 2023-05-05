# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/why/

import heapq
from sys import stdin
input = stdin.readline

def inRange(nx, ny, n):
    if nx < n and ny < n:
        if 0 <= nx and 0 <= ny:
            return True
    
    return False

def czy_jeden_z_ost(ny, nx, n):
    if ny == n - 1 or ny == n - 2:
        if nx == n - 1 or nx == n - 2:
            return True
        
    return False

def dijkstra(graf):
    odl = [[1e17 for _ in range(len(graf))] for _ in range(len(graf))]
    odl[0][0] = 0
    pq = [(0, 0, 0)]
    heapq.heapify(pq)
    while pq:
        y, x, d = heapq.heappop(pq)
        if odl[y][x] < d:
            continue
        for ny, nx, v in graf[y][x]:
            if odl[ny][nx] <= v + d:
                continue
            else:
                odl[ny][nx] = v + d
                heapq.heappush(pq, (ny, nx, odl[ny][nx]))
                
    return odl

def main():
    n, t = map(int, input().split())
    pola = []
    ruchy = [(3, 0), (0, 3), (-3, 0), (0, -3), (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (1, 0), (-1, 0), (0, -1), (0, 1)]
    graf = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        s = list(map(int, input().split()))
        pola.append(s)
        
    for y in range(n):
        for x in range(n):
            for ruch in ruchy:
                ny, nx = y + ruch[0], x + ruch[1]
                if inRange(nx, ny, n):
                    graf[y][x].append((ny, nx, pola[nx][ny] + (t * 3)))
            if czy_jeden_z_ost(y, x, n):
                if y == n - 2 and x == n - 2:
                    co_dac = (t * 2)
                else:
                    co_dac = t
                graf[y][x].append((n - 1, n - 1, co_dac))
                                      
    odl = dijkstra(graf)
    print(odl[n - 1][n - 1])              
        
    
main()