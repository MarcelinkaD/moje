# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/gra1/18756/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    dp = [-1000 for _ in range(n)]
    dp[0] = l[0]
    
    for i in range(1, n):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] + l[i])
        
    print(dp[-1])
    
main()