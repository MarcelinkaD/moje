# https://szkopul.edu.pl/problemset/problem/JDLRIKmmfMWZ7G1Sy6Ldq7m8/site/?key=statement

from sys import stdin
input = stdin.readline
import math

def main():
    n = int(input())
    s = str(input().strip())
    l = 0
    w = 0
    
    for i in range(n):
        if s[i] == "Z":
            l += 1
        else:
            w += math.ceil(l / 3)
            l = 0
            
    if l != 0:
        w += math.ceil(l / 3)
        
    print(w)
    
main()