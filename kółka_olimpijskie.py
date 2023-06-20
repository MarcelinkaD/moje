# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/koo/

from sys import stdin
input = stdin.readline

def order(x):
    return (x[1], x[0])

def main():
    n = int(input())
    kol = []
    w = 1
    
    for _ in range(n):
        a, b = map(int, input().split())
        kol.append((a, b))
        
    kol = sorted(kol, key = lambda j: order(j))
    akt_kon = kol[0][1]
    
    for i in kol:
        if i[0] >= akt_kon:
            w += 1
            akt_kon = i[1]
            
    print(w)
    
main()