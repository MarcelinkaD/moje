import math
from collections import Counter as C
from itertools import accumulate
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

def main():
    t = int(input())
    l = list(map(int, input().split()))
    glowa = -1
    ogon = 0
    akt_wyn = 0
    lenl = 0
    w = 10000000000

    while ogon < len(l) - 1:
        while glowa < len(l) - 1 and akt_wyn < t:
            lenl += 1
            glowa += 1
            akt_wyn += l[glowa]

            if akt_wyn >= t:
                w = min(lenl, w)
                
                
        akt_wyn -= l[ogon]
        ogon += 1
        lenl -= 1
        
        
        if akt_wyn >= t:
            w = min(lenl, w)
            
    print(w)


main()
