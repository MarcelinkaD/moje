# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/

from sys import stdin
input = stdin.readline

def main():
    a, b = map(int, input().split())
    s1 = (b * (b + 1)) // 2
    
    if a == 1:
        print(s1)
    else:
        a -= 1
        s2 = (a * (a + 1)) // 2
        
        print(s1 - s2)
    
main()