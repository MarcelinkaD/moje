# https://szkopul.edu.pl/c/oki-wakacje-2023/p/pma/

import math
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    od, do = map(int, input().split())
    MAXN = 100007
    sito = [1 for _ in range(MAXN)]
    sito[1], sito[0] = 0, 0
    
    for i in range(2, int(math.sqrt(MAXN))):
        if sito[i] == 1:
            for j in range(i + i, MAXN, i):
                sito[j] = 0
                
    pref = list(ac(sito))    
    w = pref[do] - pref[od - 1]
    
    print(w)
    print((do - od + 1) - w)
    
    for i in range(od, do):
        if sito[i] == 1:
            print(i, end = " ")
    
    
    
    
main()