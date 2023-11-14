# https://szkopul.edu.pl/problemset/problem/uIyU0DBwEdBOI2YO4tKPtZ1V/site/?key=statement

from sys import stdin
input = stdin.readline

def oblicz(x):
    return x * (x + 1) // 2

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    pref = [0 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + l[i - 1]
        
    pocz, kon = 0, 0
    
    while kon < n:
        while pocz < n and pref[pocz + 1] - pref[kon] > oblicz(pocz - kon + 1):
            akt_pref = pref[pocz + 1] - pref[kon]
            odl = pocz - kon + 1
            
            if oblicz(odl) == akt_pref:
                w += 1
                
                
    print(w)
    
main()