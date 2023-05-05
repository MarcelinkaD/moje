# https://szkopul.edu.pl/c/testowy_dd/p/zol/18484/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def silnia(x):
    s = 1
    
    for i in range(2, x + 1):
        s *= i
        if s > 10000:
            s %= 10000
        
    return s

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 1
    c = C(l)
    
    for key in c:
        if c[key] == 1:
            continue
        w *= silnia(c[key])
        
    if len(c) != 1:
        w *= 2
    
    if w > 10000:
        w = str(w)
        w = w[len(w) - 4 : len(w)]
        print(w)
    else:
        print(w)
    
main()