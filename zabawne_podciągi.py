# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/zab/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    pref = [0 for _ in range(n)]
    pref[0] = l[0]
    
    for i in range(1, n):
        pref[i] = pref[i - 1] + l[i]
        
    w = 0
    
    for i in range(n):
        for k in range(i, n):
            if i != 0:
                suma = pref[k] - pref[i - 1]
            else:
                suma = pref[k]
                
            if suma % 3 == 0:
                w += 1
                
    print(w)
    
main()