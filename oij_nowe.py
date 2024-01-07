# https://sio2.mimuw.edu.pl/c/oij18-1/p/oij/

import math
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    dziel = [1, 1, 1]
    ile_czego = {}
    d = 2

    while d * d <= n:
        if n % d == 0:
            n //= d
            
            if d not in ile_czego:
                ile_czego[d] = 0
                
            ile_czego[d] += 1
        else:
            d += 1
            
    if n > 1:
        if n not in ile_czego:
            ile_czego[n] = 0
            
        ile_czego[n] += 1
        
    for i in ile_czego:
        zostanie = ile_czego[i] % 3
        if zostanie == 0:
            po_ile = ile_czego[i] // 3
            dziel[0] *= i ** po_ile
            dziel[1] *= i ** po_ile
            dziel[2] *= i ** po_ile
        elif zostanie == 1:
            po_ile = ile_czego[i] // 3
            if po_ile == 0:
                dziel[0] *= i
            else:
                dziel[0] *= i ** (po_ile + 1)
                dziel[1] *= i ** po_ile
                dziel[2] *= i ** po_ile
        elif zostanie == 2:
            po_ile = ile_czego[i] // 3
            if po_ile == 0:
                dziel[0] *= i
                dziel[1] *= i
            else:
                dziel[0] *= i ** (po_ile + 1)
                dziel[1] *= i ** (po_ile + 1)
                dziel[2] *= i ** po_ile
   
   
    for i in range(dziel[0]):
        print("O", end = "")
     
    for i in range(dziel[1]):
        print("I", end = "")
        
    for i in range(dziel[2]):
        print("J", end = "")
    

    
main()