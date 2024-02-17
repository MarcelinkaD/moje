# https://szkopul.edu.pl/c/testowy_dd/p/mon/18434/

from sys import stdin
input = stdin.readline

def f(i, l, n):
    ile_sie_miesci = min(n, l[i])
    do_umieszczenia = ile_sie_miesci - i
    return do_umieszczenia

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 1
    MOD = int(1e9) + 7
    l.sort()
    
    for i in range(n):
        w *= f(i, l, n)
        w %= MOD
        
    print(w)
    
def gen(liczby, akt, l):
    if not liczby:
        for i in range(len(l)):
            if akt[i] > l[i]:
                return 0
        
        return 1
            
    w = 0 
    for i in range(len(liczby)):
        liczba = liczby[i]
        w += gen(liczby[:i] + liczby[i + 1 : len(liczby)], akt + [liczba], l)
        
    return w

def brut(n, l):
    w = gen([i + 1 for i in range(n)], [], l)
    return w

n = int(input())
l = list(map(int, input().split()))
print(brut(n, l))