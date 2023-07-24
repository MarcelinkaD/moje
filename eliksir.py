# https://szkopul.edu.pl/problemset/problem/eliksir/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n, s = map(int, input().split())
    l = []
    
    for i in range(n):
        l.append(int(input()))
        
    dp = [False for _ in range(s + 1)]
    dp[0] = True
    
    for i in range(n):
        f = l[i]
        for k in range(s, f - 1, -1):
            if dp[k - f]:
                dp[k] = True
    
    if dp[s] == True:
        print("Abrakadabra")
    else:
        print("SorryHarry")
    
main()