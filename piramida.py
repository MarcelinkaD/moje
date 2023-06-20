# https://sio2.mimuw.edu.pl/c/zwo20/p/pir/ 

from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    pola = str(input().strip())
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    
    for i in range(2, n + 1):
        if pola[i - 1] == "1":
            dp[i] = dp[i - 1]
            if i - 2 > 0:
                dp[i] += dp[i - 2]
            if i - 3 > 0:
                dp[i] += dp[i - 3]
            if i - 4 > 0:
                dp[i] += dp[i - 4]
            if i - 5 > 0:
                dp[i] += dp[i - 5]
            if i - 6 > 0:
                dp[i] += dp[i - 6]
    
    print(dp[n] % k)
            
    
main()