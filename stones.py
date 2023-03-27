# https://codeforces.com/problemset/problem/266/A

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    s = str(input())
    w = 0
    
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            w += 1
            
    print(w)
    
main()