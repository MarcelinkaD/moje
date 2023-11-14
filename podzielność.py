# https://sio2.mimuw.edu.pl/c/oij18-1/p/pod/
# Zrobione: 2, 3, 5, 6, 9, 10

import math
from collections import Counter as C
from sys import stdin
input = stdin.readline

def silnia(x):
    return math.factorial(x)

def main():
    n, k = map(str, input().split())
    ile = len(n)
    wn1 = []
    k = int(k)
    c = C(n)
    w = 0
    podz = []
    
    for i in c:
        if int(i) % k == 0 or (k == 6 and int(i) % 2 == 0):
            podz.append(i)
        
        if c[i] > 1:
            wn1.append((i, c[i]))
    
    if k == 2:
        akt = 0

        for i in podz:
            akt = silnia(ile - 1)
            przez_co = 1
            
            for k in wn1:
                if k[0] == i:
                    przez_co *= silnia(k[1] - 1)
                else:
                    przez_co *= silnia(k[1])
                    
            akt //= przez_co
            w += akt
            
    elif k == 3 or k == 9:
        suma = 0
        przez_co = 1
        
        for i in n:
            suma += int(i)
            
        if suma % 3 == 0:
            w = silnia(ile)
            
            for i in wn1:
                przez_co *= silnia(i[1])
            
            w //= przez_co
            
    elif k == 10:
        akt = 0

        for i in podz:
            akt = silnia(ile - 1)
            przez_co = 1
            
            for k in wn1:
                przez_co *= silnia(k[1])
                    
            akt //= przez_co
            w += akt
            
    elif k == 6:
        suma = 0
        przez_co = 1
        
        for i in n:
            suma += int(i)
            
        if suma % 3 == 0:
            akt = 0

            for i in podz:
                akt = silnia(ile - 1)
                przez_co = 1
                
                for k in wn1:
                    if k[0] == i:
                        przez_co *= silnia(k[1] - 1)
                    else:
                        przez_co *= silnia(k[1])
                        
                akt //= przez_co
                w += akt
                
    elif k == 5:
        akt = 0

        for i in podz:
            akt = silnia(ile - 1)
            przez_co = 1
            
            for k in wn1:
                if k[0] == i:
                    przez_co *= silnia(k[1] - 1)
                else:
                    przez_co *= silnia(k[1])
                    
            akt //= przez_co
            w += akt
            
            
    print(w)

main()