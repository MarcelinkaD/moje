# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/sil/

import bisect as bi
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    MAXPAX = int(1e13)
    silnie = []
    x = 1
    i = 2
    while True:
        if x < MAXPAX:
            silnie.append(x)
            x *= i
            i += 1
        else:
            break
    
    liczby_silne = set()
    m = len(silnie)
    
    for maska in range(1, 1 << m):
        suma_maski = 0
        for i in range(m):
            if maska & (1 << i):
                suma_maski += silnie[i]
        liczby_silne.add(suma_maski)
        
    liczby_silne = list(liczby_silne)
    liczby_silne.sort()
    pref = list(ac(liczby_silne))
    q = int(input())
    
    for _ in range(q):
        a, b = map(int, input().split())
        if a == 1:
            do = bi.bisect_right(liczby_silne, b) - 1
            print(pref[do])
        else:
            od = max(bi.bisect_left(liczby_silne, a) - 1, 0)
            do = bi.bisect_right(liczby_silne, b) - 1
            print(pref[do] - pref[od])
    
    
main()