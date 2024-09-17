# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/gra/

import math
from sys import stdin
input = stdin.readline

def dziel(x):
    wyn = set([x])
    
    for d in range(2, int(math.sqrt(x)) + 1):
        if x % d == 0:
            wyn.add(d)
            wyn.add(x // d)
            
    return wyn

def main():
    n, k = map(int, input().split())
    wykreslone = set([1])
    
    for i in range(n, n - k, -1):
        dzielniki = list(dziel(i))
        
        for i in dzielniki:
            wykreslone.add(i)
            
    w = 2
    
    while w <= n:
        if w not in wykreslone:
            print(w)
            return
        w += 1
    
    print(-1)
    
main()