# https://szkopul.edu.pl/c/testowy_dd/p/tas/18813/

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    sumy = list(ac(l))
    max_w = 1e18

    for i in range(n - 1):
        po_lewo = sumy[i]
        po_prawo = sumy[-1] - sumy[i]
        
        if abs(po_prawo - po_lewo) < max_w:
            max_w = abs(po_prawo - po_lewo)
            
    print(max_w)
    
main()