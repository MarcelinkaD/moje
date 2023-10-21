# https://szkopul.edu.pl/problemset/problem/h-Bypz8K9ECuWATsVRgym-W1/site/?key=statement

from collections import Counter as C
from sys import stdin
input = stdin.readline

def czy_podzielne(x, y):
    return x % y == 0

def main():
    n, p = map(int, input().split())
    w = 0
    li = list(map(int, input().split()))
    
    for i in range(n):
        li[i] = li[i] % p
    
    c = C(li)
    
    for i in c:
        if c[i] == 1:
            w += 1
        
    print(w)
    
main()