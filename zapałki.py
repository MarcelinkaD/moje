# https://szkopul.edu.pl/c/testowy_dd/p/zap/18430/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    akt = 1
    
    for i in range(1, n):
        if l[i - 1] == 0 and l[i] == 1:            
            if i - 1 == 0:
                w += 1
            else:
                l[i] = 0
                w += 1
            akt = 1
        else:
            akt += 1
            
    print(w)
    
main()