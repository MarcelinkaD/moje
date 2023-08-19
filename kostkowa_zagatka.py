# https://szkopul.edu.pl/c/oki-wakacje-2023/p/kza/

from sys import stdin
input = stdin.readline

def wylicz(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    
    return wylicz(x - 1) + wylicz(x - 2)
        

def main():
    x = int(input())
    if x <= 0:
        print(0)
        return
    elif x == 1:
        print(1)
        return
    elif x == 2:
        print(2)
        return
    
    dp = [0] * (x + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    print(dp[x])
    
main()