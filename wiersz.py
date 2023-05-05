# https://szkopul.edu.pl/c/testowy_dd/p/scz/25252/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def liczba_samoglosek(a, b, s):
    w1, w2 = 0, 0
    
    for i in a:
        if i in s:
            w1 += 1
            
    for i in b:
        if i in s:
            w2 += 1
            
    return w1 == w2
            

def usun_spacje(x):
    nx = x.replace(" ", "")
    return nx
    

def main():
    n, k = map(int, input().split())
    w = 0
    samogloski = ["a", "e", "i", "o", "u", "y"]
    
    for _ in range(n):
        a = str(input().strip())
        b = str(input().strip())
        a, b = usun_spacje(a), usun_spacje(b)
        
        if liczba_samoglosek(a, b, samogloski):
            if len(a) < k or len(b) < k:
                continue
            a = a[len(a) - k : len(a)]
            b = b[len(b) - k : len(b)]
            
            if a == b:
                w += 1
                
    print(w)
    
main()