# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/ca/666/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    akt_min = 1e10
    
    for i in range(n - 1, -1, -1):
        if l[i] < akt_min:
            akt_min = min(akt_min, l[i])
            w += akt_min * 
            
    print(w)
    
main()