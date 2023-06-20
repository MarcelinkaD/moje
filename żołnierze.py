# https://szkopul.edu.pl/c/testowy_dd/p/zol/18484/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def silnia(x):
    w = 1
    
    for i in range(2, x + 1):
        w *= i
        if w > 10000:
            w %= 10000
        
    return w

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 1
    c = C(l)

    for k in c:
        if c[k] == 1:
            continue
        w *= silnia(c[k])
    
    if len(c) != 1:
        w *= 2
        
    if w > 10000:
        w = str(w)
        w = w[len(w) - 4 : len(w)]
        print(w)
    else:
        print(w)
    
main()
