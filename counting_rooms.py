# https://cses.fi/problemset/task/1192

import sys
sys.setrecursionlimit(100000)
from sys import stdin
input = stdin.readline

def dfs(x, y, graf, odw, n, m, ruchy):
    odw[x][y] = True
    for move in ruchy:
        new_x = x + move[0]
        new_y = y + move[1]

        if (not inRange(new_x, new_y, n, m)):
            continue

        if (graf[new_x][new_y] == '#'):
            continue

        if (not odw[new_x][new_y]):
            dfs(new_x, new_y, graf, odw, n, m, ruchy,)

def inRange(x, y, n, m):
    return (0 <= x < n and 0 <= y < m)

def main():
    n, m = map(int, input().split())
    graf = []
    odw = [[False for _ in range(m)] for _ in range(n)]

    for i in range (n):
        graf.append(input())
      
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    w = 0
    
    for x in range(n):
        for y in range(m):
            if odw[x][y] == False and graf[x][y] == ".":
                w += 1
                dfs(x, y, graf, odw, n, m, moves)
                
    print(w)

main()    

    
    
