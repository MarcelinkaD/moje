# https://szkopul.edu.pl/problemset/problem/qpNbfeEtG6qylH6tIWzQqwx0/site/?key=statement

from sys import stdin
input = stdin.readline
import math

def czy_widzi(xr, yr, xd, yd, k):
    if xr == xd:
        if abs(yd - yr) <= k:
            return True
        else:
            return False
    elif yr == yd:
        if abs(xd - xr) <= k:
            return True
        else:
            return False
    else:
        a = abs(xr - xd)
        b = abs(yr - yd)
        
        if a + b <= k:
            return True
            
        c = math.sqrt((a ** 2) + (b ** 2))
        
        if c <= k:
            return True
        else:
            return False

def main():
    n, k, x_rat, y_rat = map(int, input().split())
    w = 0
    
    for _ in range(n):
        x_dzi, y_dzi = map(int, input().split())
        
        if czy_widzi(x_rat, y_rat, x_dzi, y_dzi, k):
            w += 1
            
    print(n - w)
        
    
main()