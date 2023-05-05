# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/wsp/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l, reverse = True)
    
    if len(l) <= 10:
        for i in l:
            print(i, end = " ")
    else:
        for i in range(10):
            print(l[i], end = " ")
    
main()