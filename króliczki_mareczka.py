# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kro1/

from sys import stdin
input = stdin.readline

def ile_od_1_do_x(x, N):
    w = 0
    d = 1
    
    while d * d <= N:
        if N % d == 0:
            if d <= x:
                w += 1
            if N // d != d:
                if N // d <= x:
                    w += 1
        d += 1
        
    return w

def main():
    n, k = map(int, input().split())
    w = [0 for _ in range(k)]
    w[0] = n
    
    for i in range(1, k):
        ile = ile_od_1_do_x(n, i)
        w[i] = ile
        
    for i in w:
        print(i, end = " ")
    
main()