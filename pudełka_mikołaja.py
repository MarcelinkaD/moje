# https://szkopul.edu.pl/problemset/problem/pudelka/site/?key=statement

import bisect as bi
from sys import stdin
input = stdin.readline

def binary(n, l):
    q = bi.bisect_left(l, n)
    if q != len(l) and l[q] == n:
        return q + 1
    else:
        return "Kup pudelko!"

def main():
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    
    for _  in range(q):
        i = int(input())
        print(binary(i, l))
    
main()