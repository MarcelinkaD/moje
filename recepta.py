# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/rec/

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    MAXN = int(2 * 1e5) + 7
    n, k, q = map(int, input().split())
    pref = [0 for _ in range(MAXN)]
    
    for _ in range(n):
        od, do = map(int, input().split())
        pref[od:do + 1] = [x + 1 for x in pref[od:do + 1]]
            
    for i in range(1, MAXN):
        if pref[i] < k:
            pref[i] = 0
        else:
            pref[i] = 1
            
    pref = list(ac(pref))
    
    for _ in range(q):
        od, do = map(int, input().split())
        
        print(pref[do] - pref[od - 1])
        
    
main()