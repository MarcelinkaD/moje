# https://szkopul.edu.pl/problemset/problem/EJyFbR6apT-0OugxvinCNzg3/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = max(a[-1], b[-1])
    
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            
    
main()