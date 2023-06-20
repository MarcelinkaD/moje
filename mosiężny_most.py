# https://sio2.mimuw.edu.pl/c/zwo20/p/mos/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = []
    
    for _ in range(n):
        l.append(int(input()))
        
    dp = [0 for _ in range(n)]
    dp[0] = l[0]
    
    if n == 1:
        print(l[0])
        return
    
    dp[1] = dp[0] + l[1]
    
    for i in range(2, n):
        index = max(dp[i - 1], dp[i - 2] + l[i])
        dp[i] = max(index, dp[i - 3] + l[i - 1] + l[i])
    
    print(dp[n - 1])
    
main()