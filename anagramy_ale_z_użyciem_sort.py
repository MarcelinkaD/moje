# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/ana/

from sys import stdin
input = stdin.readline

def main():
    a = str(input().strip())
    b = str(input().strip())
    a = "".join(sorted(a))
    b = "".join(sorted(b))
    
    if a == b:
        print("TAK")
    else:
        print("NIE")
        
    
main()