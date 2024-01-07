# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/akc/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    mini = l[0]
    wyn = 0
    
    for i in range(1, n):
        wyn = max(wyn, l[i] - mini)
        
        if l[i] < mini:
            mini = l[i]  
    
    print(wyn)
    
main()