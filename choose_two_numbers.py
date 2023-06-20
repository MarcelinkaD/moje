# https://codeforces.com/problemset/problem/1206/A

import bisect as bi
from sys import stdin
input = stdin.readline

def binary(li, n):
    q = bi.bisect_left(li, n)
    if q != len(li) and li[q] == n:
        return q
    else:
        return - 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    for i in a:
        for k in b:
            if binary(a, i + k) == -1 and binary(b, i + k) == -1:
                print(i, k)
                return 
    
main()