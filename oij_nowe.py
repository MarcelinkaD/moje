# https://sio2.mimuw.edu.pl/c/oij18-1/p/oij/

import math
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    MAXN = int(104)
    sito = [0, 1] * (MAXN//2) + [1]
    sito[1], sito[2] = 0, 1
    dziel = []
        
    for i in range(3, int(MAXN**0.5+1), 2):
        if sito[i] == 1:
            sito[i*i::2*i] = [0] * int((MAXN+2*i-1-i*i)/(2*i))
            
    while n % 2 == 0:
        dziel.append(2)
        n = n // 2
         
    for i in range(1, int(math.sqrt(n))+1, 2):
        if sito[i] == 1:
            while n % i == 0:
                dziel.append(i)
                n = n // i
                
    while len(dziel) > 3:
        dziel[1] += dziel[0]
        dziel.pop(0)
        
    for k in range(dziel[0]):
        print("O", end = "")
            
    for k in range(dziel[1]):
        print("I", end = "")
        
    for k in range(dziel[2]):
        print("J", end = "")
    
main()