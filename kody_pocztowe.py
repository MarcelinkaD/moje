# https://solve.edu.pl/contest/root-wsi-diveasy-s40/problem/1539/view

from sys import stdin
input = stdin.readline

def main():
    s = str(input().strip())
    n = len(s)
    od_lewo, od_prawo = [0 for _ in range(n)], [0 for _ in range(n)]
    
    for i in range(1, n):
        od_lewo[i] = od_lewo[i - 1]
        if s[i - 1] != "-":
            od_lewo[i] += 1
            
    for i in range(n - 2, -1, -1):
        od_prawo[i] = od_prawo[i + 1]
        if s[i + 1] != "-":
            od_prawo[i] += 1
            
    w = 0
    
    for i in range(n):
        if s[i] == "-":
            nl, np = od_lewo[i], od_prawo[i]
            if nl >= 2 and np >= 3:
                w += 

main()