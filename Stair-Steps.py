# https://py.checkio.org/en/mission/stair-steps/

def checkio(l):
    n = len(l)
    l.append(0)
    dp = [0 for _ in range(n + 1)]
    dp[0] = l[0]
    dp[1] = max(l[1], dp[0] + l[1])
    
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1] + l[i], dp[i - 2] + l[i])
        
    return dp[-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([5, -3, -1, 2]) == 6, "Fifth"
    assert checkio([5, 6, -10, -7, 4]) == 8, "First"
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, "Second"
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, "Third"
    assert checkio([5,4,3,-99,2,-20]) == 14, ":("
    print("All ok")

