# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/ana/

import bisect as bi
from sys import stdin
input = stdin.readline

def binary(li, n):
    q = bi.bisect_left(li, n)
    if q != len(li) and li[q] == n:
        return q + 1
    else:
        return "Kup pudelko!"

def main():
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    
    for _ in range(q):
        zap = int(input())
        w = binary(l, zap)
        print(w)
    
main()