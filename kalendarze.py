# https://szkopul.edu.pl/c/testowy_dd/p/kal/18977/

import bisect as bi
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def calkowita_zam(dzien, mies, pref):
    gdzie = bi.bisect_left(pref, dzien)
    dzien -= pref[gdzie - 1]
    mies = gdzie
    return (dzien, mies)

def zamiana_dni(dzien, mies, pref):
    if mies != 1:
        dzien += pref[mies - 1]
    return dzien

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    a.insert(0, 0)
    b.insert(0, 0)
    prefa = list(ac(a))
    prefb = list(ac(b))
    
    for _ in range(q):
        dzien, mies, kto = map(str, input().split())
        dzien, mies = int(dzien), int(mies)
        
        if kto == "A":
            dzien = zamiana_dni(dzien, mies, prefa)
            dzien, mies = calkowita_zam(dzien, mies, prefb)
        else:
            dzien = zamiana_dni(dzien, mies, prefb)
            dzien, mies = calkowita_zam(dzien, mies, prefa)
        
        print(dzien, mies)
    
main()