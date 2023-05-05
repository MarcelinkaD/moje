# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2022-23/p/skr/18424/

import math
from sys import stdin
input = stdin.readline

def czy_pierwsza(p):
    if p == 0 or p == 1:
        return False
    
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False

    return True

def czy_skr(n):
    s = str(n)
    pr = ""
    for k in s:
        pr += k
        if czy_pierwsza(int(pr)) == False:
            return False
    
    return True

def main():
    od, do = map(int, input().split())
    w = 0
    
    for i in range(od, do + 1):
        if czy_skr(i):
            w += 1
    print(w)
    
main()