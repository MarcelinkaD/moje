# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/liz/17289/

from sys import stdin
input = stdin.readline

def order(x):
    return x[0]

def binary(l, co):
    pocz = 0
    end = len(l)
    while pocz < end:
        s = (pocz + end) // 2
        if l[s][0] < co:
            pocz = s + 1
        else:
            end = s
            
    return pocz

def main():
    n, q = map(int, input().split())
    liz = str(input().strip())
    prze = []
    
    for i in range(len(liz)):
        akt = 0
        for k in range(i, len(liz)):
            if liz[k] == "T":
                akt += 2
            else:
                akt += 1
            prze.append((akt, i, k))
            
    prze = sorted(prze, key = lambda j: order(j))
    
    for _ in range(q):
        z = int(input())
        w = prze[binary(prze, z)]
        if w[0] == z:
            print(w[1] + 1, end = " ")
            print(w[2] + 1)
        else:
            print("NIE")
    
    
main()