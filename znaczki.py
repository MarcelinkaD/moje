# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/zna/

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    dawl = len(set1)
    set1.update(set2)
    
    print(len(set1) - dawl)
    
main()
