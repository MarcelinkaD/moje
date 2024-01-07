# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/ca/666/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    akt_min = l[-1]
    min_poz_na_prawo = [0 for _  in range(n)]
    
    for i in range(n - 1, -1, -1):
        if l[i] < akt_min:
            akt_min = l[i]
        min_poz_na_prawo[i] = akt_min
        
            
    akt_min = min_poz_na_prawo[-1]
    pop = n - 1
            
    for i in range(n - 1, -1, -1):
        if akt_min > min_poz_na_prawo[i]:
            w += (pop - i) * akt_min 
            akt_min = min_poz_na_prawo[i]
            pop = i
            

    w += (pop + 1) * akt_min 
            
    print(w)
    
main()