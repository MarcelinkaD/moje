# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/wsp/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse = True)
    
    if n <= 10:
        for i in l:
            print(i, end = " ")
    else:
        for i in range(10):
            print(l[i], end = " ")
    
main()