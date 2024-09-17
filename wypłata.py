# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/wyp/

from math import factorial
from sys import stdin
input = stdin.readline

def f(n):
    wyn = 0
    
    wyn = n * (n + 1) // 2
    
    return wyn

def main():
    s = str(input().strip())
    akt_w = 1
    w = 0
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            akt_w += 1
        else:
            w += f(akt_w)
            akt_w = 1
            
    w += f(akt_w)
    
    print(w)
    
main()