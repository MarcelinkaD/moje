# https://szkopul.edu.pl/c/oki-poziom-2-20232024/p/dia/

from sys import stdin
input = stdin.readline

def main():
    MAX_N = int(1e6 + 9)
    n, k = map(int, input().split())
    tab = list(map(int, input().split()))
    dp = [0 for _  in range(MAX_N)]
    dp[0] = 1
    MOD = int(1e9 + 9)
    
    for i in range(n):
        dp[tab[i]] = (dp[tab[i]] + dp[tab[i] - 1]) % MOD
        
    print(dp[k])
    
main()