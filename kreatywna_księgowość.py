# https://szkopul.edu.pl/problemset/problem/dS891CqofUdR0QKngPnX6IH6/site/?key=statement

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    pref = list(ac(l))
    w = -1e19
    
    for i in range(n):
        for k in range(i, n):
            if i != 0:
                roznica = pref[k] - pref[i - 1]
            else:
                roznica = pref[k]
            po_mod = roznica % m
            w = max(w, po_mod)
    
    print(w)
    
main()