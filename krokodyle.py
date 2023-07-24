# https://main2.edu.pl/c/konkurs-podstaw-algorytmiki/p/kro/

from sys import stdin
input = stdin.readline

def potega(a, b, MOD):
    if b == 0:
        return 1
    
    w = potega(a, b // 2, MOD)
    w = (w * w) % MOD
    
    if b % 2 == 1:
        w = (w * a) % MOD
    
    return w

def main():
    q = int(input())
    
    for _ in range(q):
        a, b = map(int, input().split())
        print(potega(a + 1, b, 10000))
        
main()