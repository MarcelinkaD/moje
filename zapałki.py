# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/zap/18430/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    pop = l[0]
    
    for i in range(1, n):
        if pop == 0 and l[i] == 1:
            w += 1
            pop = 0
        else:
            pop = l[i]
            
            
    print(w)
    
main()