# https://www.spoj.com/problems/OPCPRIME/

import math
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    MAXN = int(1e12) + 7
    sito = [0 for _ in range(MAXN)]
    sito[0], sito[1] = 0, 0
    
    for i in range(2, MAXN):
        if sito[i] == 0:
            for k in range(i, MAXN, i):
                if sito[k] == 0:
                    sito[k] = i
    
    w = set([])
    while n != 1:
        w.add(sito[n])
        n //= sito[n]
        
    w = list(w)
    w.sort()
    
    for i in w:
        print(i)
    
main()