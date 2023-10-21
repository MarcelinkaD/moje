# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kal/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    qu = list(map(int, input().split()))
    pref = [0 for _  in range(n + 1)]
    l.insert(0, 0)
    
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + l[i]
        
    pary = []
    
    for i in range(0, q * 2, 2):
        pary.append((qu[i], qu[i + 1]))
    
    for i in range(q):
        od, do = pary[i][0], pary[i][1]
        print(pref[do] - pref[od - 1])
    
main()