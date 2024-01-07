# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kos/18466/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    pocz, v = map(int, input().split())
    
    for i in range(n):
        gdzie, w = map(int, input().split())
        if w > v:
            za_ile = (pocz - gdzie) // (w - v)
        
        
        
        

main()