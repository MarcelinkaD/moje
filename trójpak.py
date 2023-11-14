# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/tro/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ile_czego = list(map(int, input().split()))
    co_musimy = set()
    co_mamy = set()
    w = 0
    
    for i in range(3):
        for k in range(ile_czego[i]):
            co_musimy.add(i + 1)
    
    ogon, glowa = 0, -1
    
    while ogon < n - 1:
        while glowa < n - 1 and len(co_mamy) < len(co_musimy):
            glowa += 1
            co_mamy.add(l[glowa])
            
            if co_mamy == co_musimy:
                w += 1
            
        co_mamy.remove(l[ogon])
        ogon += 1
        
    print(w)
main()