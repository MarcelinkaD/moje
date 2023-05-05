# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/min/18478/

import bisect as bi 
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    w = 0
    
    while True:
        w += k
        g = bi.bisect_left(l, w) 
        if g == n or l[g] != w:
            print(w)
            break
    
main()