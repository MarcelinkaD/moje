# https://szkopul.edu.pl/problemset/problem/LWpMcXylQBa6wHzcJ6U7axzK/site/?key=statement

import bisect as bi
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def zamiana_dni(dzien, mies, pref):
    if mies != 1:
        dzien += pref[mies - 1]
    return dzien

def calkowita_zam(dzien, mies, pref):
    gdzie = bi.bisect_left(pref, dzien)
    dzien -= pref[gdzie - 1]
    mies = gdzie
    return (dzien, mies)

def main():
    la, lb = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    a.insert(0, 0)
    b.insert(0, 0)
    suma = list(ac(a))
    sumb = list(ac(b))
    
    for _ in range(q):
        dz, mies, lit = map(str, input().split())
        dz, mies = int(dz), int(mies)
        
        if lit == "A":
            dz = zamiana_dni(dz, mies, suma)            
            dz, mies = calkowita_zam(dz, mies, sumb)
        else:
            dz = zamiana_dni(dz, mies, sumb) 
            dz, mies = calkowita_zam(dz, mies, suma)
        
        print(dz, mies)
        
        
        
    
main()