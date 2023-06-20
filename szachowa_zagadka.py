# https://szkopul.edu.pl/c/oki-wakacje-2023/p/sza/

from sys import stdin
input = stdin.readline
import math

def pot(a, b):
    return math.pow(a, b)

def main():
    q = int(input())
    
    for _ in range(q):
        i, n = map(int, input().split())
        w = int(pot(2, i - 1))
        
        if w > n:
            print(w - n)
        else:
            print("TAK")
    
main()