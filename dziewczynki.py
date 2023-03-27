# https://szkopul.edu.pl/c/testowy_dd/p/dzi/18863/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    min_w = 1e18
    glowa = -1
    ogon = 0
    ld, lc = 0, 0
    c = C(l)
    
    if 0 not in c:
        print("NIE")
        return 0
    
    if c[0] < k:
        print("NIE")
        return 0
    
    while ogon < n - 1:
        while glowa < n - 1 and ld != k:
            glowa += 1
            
            if l[glowa] == 0:
                ld += 1
            else:
                lc += 1
                
            if ld == k:
                min_w = min(lc, min_w)
            
        if l[ogon] == 0:
            ld -= 1
        else:
            lc -= 1
                
        if ld == k:
            min_w = min(lc, min_w)
                
        ogon += 1
                
    if min_w != 1e18:
        print(min_w)
    else:
        print("NIE")
    
main()
