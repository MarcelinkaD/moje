# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/wyp/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(str, input().strip().split()))
    c = C(l)
    q = int(input())
    ziuba = list(map(str, input().strip().split()))
    
    for i in ziuba:
        if i in c:
            print(i, c[i])
        else:
            print("Kolego tutaj nie ma niczego!")
    
main()