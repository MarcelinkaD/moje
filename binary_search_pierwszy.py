# https://szkopul.edu.pl/problemset/problem/bsp/site/?key=statement

import bisect as bi
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    lewo, prawo = 0, n
    
    while lewo < prawo:
        s = (lewo + prawo) // 2
        if l[s] < q:
            lewo = s + 1
        else:
            prawo = s
            
    print(lewo + 1)
    
main()