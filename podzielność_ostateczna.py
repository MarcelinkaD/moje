# https://sio2.mimuw.edu.pl/c/oij18-1/p/pod/

from sys import stdin
input = stdin.readline

def gen(lit, k, akt, schowek):
    if not lit:
        return 1 if akt == 0 else 0
    
    klucz = (tuple(lit), akt)
    
    if klucz in schowek:
        return schowek[klucz]
    
    wyn = 0
    czy = set()
    for i in range(len(lit)):
        litera = lit[i]
        if litera not in czy:
            wyn += gen(lit[:i] + lit[i+1:], k, (akt * 10 + litera) % k, schowek)
            czy.add(litera)
    
    schowek[klucz] = wyn
    
    return wyn

def fast(n, k):
    k = int(k)
    lit = [int(i) for i in n]  # Przechowuje cyfry jako liczby całkowite
    
    schowek = {}
    w = gen(lit, k, 0, schowek)   
    
    print(w)    

n, k = input().split()
fast(n, k)