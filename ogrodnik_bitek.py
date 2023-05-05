# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/ogr/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    c = C(l)
    podlane = set()
    
    for _ in range(q):
        kwiat = int(input())
        if kwiat in c:
            if kwiat not in podlane:
                c[kwiat] -= 1
                print("NIEPODLANY", c[kwiat])
                podlane.add(kwiat)
            else:
                c[kwiat] -= 1
                print("PODLANY", c[kwiat])                
        else:
            print("BRAK")
    
main()