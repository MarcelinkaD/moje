# https://szkopul.edu.pl/c/oki-wakacje-2023/p/koi/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    koty = list(map(int, input().split()))
    wkladki = list(map(int, input().split()))
    c = dict(C(wkladki))
    w = [0 for _ in range(n)]
    
    for i in range(n):
        kot = koty[i]
        akt_w = 0
        if kot in c:
            akt_w += c[kot]
        if kot - 1 in c:
            akt_w += c[kot - 1]
        if kot + 1 in c:
            akt_w += c[kot + 1]
            
        w[i] = akt_w
        
    for i in w:
        print(i, end = " ")
    
    
main()