# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/abr1/

from sys import stdin
input = stdin.readline

def main():
    dane = list(map(int, input().strip().split()))
    n, m = dane[0], dane[1]
    kol = dane[2:2+n]
    ludzie = dane[2+n:2+n+m]
        
    lkol, ll = 0, 0
    w = 0
    kol.sort()
    ludzie.sort()
    
    while ll < m:
        if kol[lkol] < ludzie[ll]:
            w += ludzie[ll] - kol[lkol]
            lkol += 1
            if lkol == n:
                break
        
        ll += 1
              
    if lkol == n:
        print("TAK")
        print(w)
    else:
        print("NIE")
    
main()