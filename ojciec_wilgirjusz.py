# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/wir/

import bisect as bi
from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    sumy = list(ac(l))
    
    if n == 1:
        print(l[0])
    else:
        mini = 1e18
        w = -1
        for i in range(n):
            if i != n - 1 and i != 0:
                odl1 = sumy[i - 1]
                odl2 = (sumy[-1] - sumy[i])
                if abs(odl1 - odl2) < mini:
                    mini = abs(odl1 - odl2)
                    w = i
                    
            elif i == n - 1:
                if sumy[i - 1] < mini:
                    mini = sumy[i - 1]
                    w = i
            
            else:
                if sumy[-1] - sumy[0] < mini:
                    mini = sumy[-1] - sumy[0]
                    w = i
            
        print(l[w])
    
main()