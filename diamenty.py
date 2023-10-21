# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/dia/

from sys import stdin
input = stdin.readline

def in_range(y, x, n, m):
    if y > -1 and y < n:
        if x > -1 and x < m:
            return True
    return False

def main():
    q = int(input())
    
    for _ in range(q):
        m, n = map(int, input().split())
        l = []
        
        for _ in range(n):
            tab = list(map(int, input().split()))
            
            l.append(tab)
            
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        if l[0][0] == 1:
            dp[0][0] = 1
            
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + l[i][0]
        
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + l[0][j]
            
        for i in range(1, n):
            for k in range(1, m):
                dp[i][k] = max(dp[i - 1][k], dp[i][k - 1]) + l[i][k]

                        
        
        print(dp[n - 1][m - 1])
        
main()