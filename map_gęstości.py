# https://szkopul.edu.pl/problemset/problem/0QusZwo2JAyvhPj1JIKRc8H7/site/?key=statement

from sys import stdin
input = stdin.readline

def suma(i1, j1, i2, j2, pref):
    return pref[i2][j2] - pref[i1 - 1][j2] - pref[i2][j1 - 1] + pref[i1 - 1][j1 - 1]

def main():
    n, r = map(int, input().split())
    l = []
    
    for _ in range(n):
        i = list(map(int, input().split()))
        l.append(i)
        
    pref = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + l[i - 1][j - 1]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(suma(max(1, i - r), max(1, j - r), min(n, i + r), min(n, j + r), pref), end=" ")
        print("")
    
main()
