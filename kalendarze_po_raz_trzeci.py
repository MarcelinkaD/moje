# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kal1/18977/

from bisect import bisect_left as bi
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    prefa, prefb = list(ac(a)), list(ac(b))
    prefa.insert(0, 0)
    prefb.insert(0, 0)
    
    for _ in range(q):
        dzien, mies, lit = map(str, input().split())
        dzien = int(dzien)
        mies = int(mies)
        wd, wm = 0, 0
        
        if lit == "A":
            if mies != 1:
                dni = dzien + prefa[mies - 1]
            else:
                dni = dzien
            gdzie = bi(prefb, dni)
            dni -= prefb[gdzie - 1]
            wm = gdzie
            wd = dni
        else:
            if mies != 1:
                dni = dzien + prefb[mies - 1]
            else:
                dni = dzien
            gdzie = bi(prefa, dni)
            dni -= prefa[gdzie - 1]
            wm = gdzie
            wd = dni
            
            
        print(wd, wm)
    
main()