# https://szkopul.edu.pl/problemset/problem/wizyta/site/?key=statement

import bisect as bi
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    rodz = list(map(int, input().split()))
    ile = list(map(int, input().split()))
    n_rodz = []
    q = int(input())        
    
    for i in range(n):
        for _ in range(ile[i]):
            n_rodz.append(rodz[i])
    
    n_rodz.sort(reverse = True)
    pref = list(ac(n_rodz))
    
    for _ in range(q):
        wag = int(input())
        g = bi.bisect_left(pref, wag)
        if g != len(pref):
            print(g + 1)
        else:
            print(g)
            
    
main()