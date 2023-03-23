# https://szkopul.edu.pl/c/testowy_dd/p/wie/18801/

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
        
    for i in ludki:
        gdzie = bi.bisect_left(schodki, i)
        print(gdzie, end = " ")
    
main()