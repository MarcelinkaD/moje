# https://sio2.mimuw.edu.pl/c/oij18-1/p/pod/

import math
from sys import stdin
input = stdin.readline

def main():
    n, k = map(str, input().split())
    k = int(k)
    zlicz = [0 for _ in range(10)]
    suma = 0
    
    for i in n:
        zlicz[int(i)] += 1
        suma += int(i)
    
    if k == 10:
        if zlicz[0] != 0:
            pozostalo = len(n) - 1
            w = math.factorial(pozostalo)
        else:
            w = 0
    elif k == 3:
        
        
    print(w)
    
main()