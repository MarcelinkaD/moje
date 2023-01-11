from sys import stdin
input = stdin.readline

def mod(a, b):
    return a % b

def main():
    MOD = 1000000007
    n, l, r, k = map(int, input().split())
    dp = [[[0] for _ in range(k)] for _ in range(n)]
    cnt = [0] * k
    
    for i in range(k):
        pomocna_zmienna = mod(r, k) - mod(l, k) % MOD
        dp[0][i] = pomocna_zmienna
        cnt[i] = pomocna_zmienna
        
    for i in range
    
main()