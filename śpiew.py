# https://szkopul.edu.pl/problemset/problem/JDLRIKmmfMWZ7G1Sy6Ldq7m8/site/?key=statement

import math
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = str(input().strip())
    akt = 0
    w = 0
    
    for i in range(n):
        if l[i] == "Z":
            akt += 1
        if l[i] == "W" or i == n - 1:
            w += math.ceil(akt / 3)
            akt = 0
            
        
            
    print(w)
    
main()