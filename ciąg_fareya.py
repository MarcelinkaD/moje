# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/far/

import math 
from sys import stdin
input = stdin.readline

def order(x):
    return x[0] / x[1]

def max_skroc(licz, mia):
    dz = int(math.gcd(licz, mia))
    mia //= dz
    licz //= dz
    return (licz, mia)

def main():
    n = int(input())
    ciag = [(0, 1)]
    
    for i in range(1, n + 1):
        for k in range(i, n + 1):
            if i < k:
                licz, mia = max_skroc(i, k)
                ciag.append((licz, mia))
    
    ciag = list(set(ciag))
    ciag = sorted(ciag, key = lambda j: order(j))
    
    for i in ciag:
        print(str(i[0]) + "/" + str(i[1]), end = " ")
        
    print("1/1")
    
main()