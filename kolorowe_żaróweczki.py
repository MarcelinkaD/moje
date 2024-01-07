# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kza/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ost = {}
    pie = {}
    mini = 1e18
    maxi = 0
    
    for i in range(n):
        if l[i] not in pie:
            pie[l[i]] = i
        else:
            now_mini = i - ost[l[i]]
            now_maxi = i - pie[l[i]]
            
            maxi = max(maxi, now_maxi)
            mini = min(mini, now_mini)
            
        ost[l[i]] = i
        
    if mini == 1e18:
        mini = 0
        
    print(mini, maxi)
    
main()