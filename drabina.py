# https://szkopul.edu.pl/problemset/problem/HP7pSEAJ_bJo48SU52zVi2c4/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    
    for _ in range(q):
        n, p = map(int, input().split())
        dp = [0 for _ in range(n + 1)]
        
        if n == 1:
            print(1 % 2 ** p)
        elif n == 2:
            print(2 % 2 ** p)
        elif n == 3:
            print(3 % 2 ** p)
        else:
            dp[1] = 1
            dp[2] = 2
            
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
                
            print(dp[n] % 2 ** p)
    
main()