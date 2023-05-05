# https://szkopul.edu.pl/c/testowy_dd/p/scz/25252/

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.reverse()
    pref = list(ac(l))
    pref.reverse()
    
    for i in pref:
        print(i, end = " ")
    
main()