# https://szkopul.edu.pl/problemset/problem/QgFenN44XX_a8nX7RPmBNph4/site/?key=statement

import bisect as bi
from sys import stdin
input = stdin.readline

def binary(li, co, od):
    pocz = od
    kon = len(li) - 1
    
    while pocz < kon:
        sr = (pocz + kon) // 2
        if li[sr] >= co:
            kon = sr
        elif li[sr] < co:
            pocz = sr + 1
            
    return max(0, pocz - 1)
    
    
def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    maxi = l[n - 1]
    w = 0
    bitek = 2
    od = 0
    
    while bitek < maxi:
        jaka = binary(l, bitek, od)
        
        if l[jaka] < bitek:
            od = jaka
            bitek += l[jaka]
            w += 1
        else:
            if bitek >= maxi:
                break
            else:
                print("NIE")
                return 0
    print(w)
    
    
main()