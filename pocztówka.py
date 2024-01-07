# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/poc/

from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    w = 0
    do = 0
    
    for i in range(n):
        if l[i] >= k:
            ile_po_prawej = n - i - 1
            ile_po_lewej = i - do
            lewo_i_prawo = ile_po_lewej * ile_po_prawej
            
            w += ile_po_prawej + lewo_i_prawo + ile_po_lewej + 1 
            
            do = i + 1
            
    print(w)
              
    
main()