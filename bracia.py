# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/bra/18442/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    ost = {}
    pie = {}
    wolne = 0
    
    for i in range(n):
        if l[i] not in pie:
            pie[l[i]] = i
            
    for i in range(n - 1, -1, -1):
        if l[i] not in ost:
            ost[l[i]] = i
    
    for i in range(n):
        if i == ost[l[i]] and pie[l[i]] >= wolne:
            w += 1
            wolne = i + 1
            
    print(w)
    
main()


