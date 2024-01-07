# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/tro/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ile_czego = list(map(int, input().split()))
    co_musimy = {1 : 0, 2 : 0, 3: 0}
    co_mamy = {1 : 0, 2 : 0, 3: 0}
    w = 0
    ile_cyfr = 0
    suma = 0
    
    for i in range(3):
        co_musimy[i + 1] = ile_czego[i]
        ile_cyfr += ile_czego[i]
    
    ogon, glowa = 0, -1
    
    while ogon < n:
        while glowa < n - 1 and suma < ile_cyfr:
            glowa += 1
            co_mamy[l[glowa]] += 1
            suma += 1
            
            if co_mamy == co_musimy:
                w += 1
            
        co_mamy[l[ogon]] -= 1
        ogon += 1
        suma -= 1
        
        if co_mamy == co_musimy:
            w += 1
        
    print(w)
main()