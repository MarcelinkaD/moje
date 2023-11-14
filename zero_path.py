# https://codeforces.com/problemset/problem/1788/E

def max_min_path_sum(t, test_cases):
    maxn = 1007 
    dp = [[[0] * 2 for _ in range(maxn)] for _ in range(maxn)] 

    results = []

    for _ in range(t):
        n, m = test_cases[_][0], test_cases[_][1]
        grid = test_cases[_][2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                x = grid[i-1][j-1]
                if i == 1 and j == 1:
                    dp[i][j][0] = dp[i][j][1] = x
                elif i > 1 and j == 1:
                    dp[i][j][0] = dp[i][j][1] = dp[i-1][j][1] + x
                elif j > 1 and i == 1:
                    dp[i][j][0] = dp[i][j][1] = dp[i][j-1][1] + x
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + x
                    dp[i][j][1] = min(dp[i-1][j][1], dp[i][j-1][1]) + x
        
        if not ((n + m) & 1):
            results.append("NO")
        elif dp[n][m][0] >= 0 and dp[n][m][1] <= 0:
            results.append("YES")
        else:
            results.append("NO")

    return results

def main():
    t = int(input().strip())

    test_cases = []
    for _ in range(t):
        n, m = map(int, input().strip().split())
        grid = [list(map(int, input().strip().split())) for _ in range(n)]
        test_cases.append((n, m, grid))


    results = max_min_path_sum(t, test_cases)
    

    for res in results:
        print(res)


main()
