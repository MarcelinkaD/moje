# https://szkopul.edu.pl/problemset/problem/qY5rn-N0HxgKREU1d-8s2bJl/site/?key=statement

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.reverse()
    pref = list(ac(l))
    
    for i in range(n - 1, -1, -1):
        print(pref[i], end = " ")    
    
main()