# https://szkopul.edu.pl/problemset/problem/Rf4E0AVIQ6vprRVEvdvj17dp/site/?key=statement

from sys import stdin
input = stdin.readline

def read_input():
    n = int(input())
    try:
        tab = list(map(int, input().split()))
        if len(tab) < n:
            for _ in range(n - len(tab)):
                tab.append(int(input()))
    except ValueError:
        tab = [int(input()) for _ in range(n)]
    return (n, tab)

def gen(liczby, akt, akt_budzet):
    if not liczby:
        return 1
    
    w = 0
    for i in range(len(liczby)):
        liczba = liczby[i]
        if akt_budzet + liczba >= 0:
            w += gen(liczby[:i] + liczby[i + 1:], akt + [liczba], akt_budzet + liczba)
            
    return w
    

def brut():
    MOD = int(1e9) + 7
    n, l = read_input()
    
    w = gen(l, [], 0)
    
    print(w % MOD)
    
brut()