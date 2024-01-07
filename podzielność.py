# https://sio2.mimuw.edu.pl/c/oij18-1/p/pod/
# Zrobione: 2, 3, 5, 6, 9, 10

import math
from collections import Counter as C
from sys import stdin
input = stdin.readline

def gen(lit, k, akt, schowek):
    if not lit:
        if akt == 0:
            return 1
        return 0
    
    klucz = (tuple((lit)), akt)
    
    if klucz in schowek:
        return schowek[klucz]
    
    wyn = 0
    czy = set()
    for i in range(len(lit)):
        litera = lit[i]
        if litera not in czy:
            wyn += gen(lit[:i] + lit[i+1:], k, ((akt * 10) + int(lit[i])) % k, schowek)
            czy.add(litera)
    
    schowek[klucz] = wyn
    
    return wyn

def silnia(x):
    return math.factorial(x)

def main():
    n, k = map(str, input().split())
    ile = len(n)
    wiecej_niz_1 = []
    k = int(k)
    zlicz = C(n)
    w = 0
    liczby_odpowiednie = []
    
    for i in zlicz:
        if int(i) % k == 0 or (k == 6 and int(i) % 2 == 0):
            liczby_odpowiednie.append(i)
        
        if zlicz[i] > 1:
            wiecej_niz_1.append((i, zlicz[i]))
    
    if k == 2 or k == 10 or k == 5:
        akt = 0

        for i in liczby_odpowiednie:
            akt = silnia(ile - 1)
            przez_co = 1
            
            for j in wiecej_niz_1:
                if j[0] == i:
                    przez_co *= silnia(j[1] - 1)
                else:
                    przez_co *= silnia(j[1])
                    
            akt //= przez_co
            w += akt
            
    elif k == 3 or k == 9:
        suma = 0
        przez_co = 1
        
        for i in n:
            suma += int(i)
            
        if suma % 3 == 0:
            w = silnia(ile)
            
            for i in wiecej_niz_1:
                przez_co *= silnia(i[1])
            
            w //= przez_co
            
    elif k == 6:
        suma = 0
        przez_co = 1
        
        for i in n:
            suma += int(i)
            
        if suma % 3 == 0:
            akt = 0

            for i in liczby_odpowiednie:
                akt = silnia(ile - 1)
                przez_co = 1
                
                for j in wiecej_niz_1:
                    if j[0] == i:
                        przez_co *= silnia(j[1] - 1)
                    else:
                        przez_co *= silnia(j[1])
                        
                akt //= przez_co
                w += akt
        
    else:
        lit = []
        schowek = {}
        
        for i in n:
            lit.append(i)
        
        w = gen(lit, k, 0, schowek)
    
        
    print(w)

main()