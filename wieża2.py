# https://szkopul.edu.pl/c/testowy_dd/p/wiz/18819/

import bisect as bi
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    schodki = list(map(int, input().split()))
    ludki = list(map(int, input().split()))
    maxi = -1
    
    for i in range(n):
        maxi = max(schodki[i], maxi)
        schodki[i] = maxi
        
    do = n
    
    for i in range(m):
        gdzie = bi.bisect_left(schodki, ludki[i], lo = 0, hi = do)
        do = max(gdzie - 1, 0)
        print(gdzie, end = " ")
    
main()