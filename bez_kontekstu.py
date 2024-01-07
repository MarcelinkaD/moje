# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/r1d/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    l1 = str(input().strip())
    l2 = str(input().strip())
    w = []
    
    glowa, ogon = m - 1, 0
    musimy = dict(C(l2))
    mamy = dict(C(l1[ogon : glowa + 1]))
    
    while glowa < n - 1:
        if mamy == musimy:
            w.append(ogon + 1)
            
        glowa += 1
        
        if l1[glowa] not in mamy:
            mamy[l1[glowa]] = 0
            
        mamy[l1[glowa]] += 1
        mamy[l1[ogon]] -= 1
        
        if mamy[l1[ogon]] == 0:
            del mamy[l1[ogon]]
            
        ogon += 1
        
    if mamy == musimy:
        w.append(ogon + 1)
        
    print(len(w))
    
    for i in w:
        print(i, end = " ")
    
main()