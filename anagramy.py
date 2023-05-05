# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/ana/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    s1 = str(input().strip())
    s2 = str(input().strip())
    c1 = C(s1)
    c2 = C(s2)
    
    if c1 == c2:
        print("TAK")
    else:
        print("NIE")
    
main()