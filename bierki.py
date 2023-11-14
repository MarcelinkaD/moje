# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/bie/18490/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = []
    
    for _ in range(n):
        l.append(int(input()))
        
    l.sort()
    glowa, ogon, akt_w, w = 1, 0, 1, -1
    
    while ogon < n:
        while glowa < n and l[glowa] < l[ogon] + l[ogon + 1]:
            glowa += 1
            akt_w += 1
            w = max(akt_w, w)
            
        akt_w -= 1
        ogon += 1
        
    print(w)
    
main()