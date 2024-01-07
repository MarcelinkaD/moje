# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/zak/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, m, s = map(int, input().split())
    ch = list(map(int, input().split()))
    dz = list(map(int, input().split()))
    c = dict(C(ch))
    w = 0
    
    for i in dz:
        potrzeba = s - i
        
        if potrzeba in c:
            w += c[potrzeba]
            
    print(w)
    
main()