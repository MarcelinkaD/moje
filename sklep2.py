# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/skl/27406/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    w = {}
    
    for _ in range(n):
        a, k = map(int, input().split())
        
        if a not in w:
            w[a] = 0
        w[a] += k
        
    print(len(w))
    for i in w:
        print(i, w[i])
    
main()