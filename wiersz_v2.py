# https://szkopul.edu.pl/c/testowy_dd/p/wie2/24149/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def zamien(x):
    return x.replace(" ", "")

def ile_samo(x, samo):
    s = 0
    
    for i in samo:
        if i in x:
            s += x[i]
            
    return s

def main():
    n, k = map(int, input().split())
    w = 0
    samo = ["a", "e", "i", "o", "u", "y"]
    
    for _ in range(n):
        a = str(input().strip())
        b = str(input().strip())
        a = zamien(a)
        b = zamien(b)
        
        if len(a) < k or len(b) < k:
            continue
        
        ca, cb = dict(C(a)), dict(C(b))
        
        if ile_samo(ca, samo) == ile_samo(cb, samo):
            if a[len(a) - k : len(a)] == b[len(b) - k : len(b)]:
                w += 1
            
    print(w)

main()