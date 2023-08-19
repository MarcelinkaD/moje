# https://py.checkio.org/en/mission/knapsack-problem-2/

def knapsack(weight, items):
    wagi = []
    wartosci = []
    
    for i in items:
        if len(i) == 3:
            for _ in range(i[2]):
                wagi.append(i[1])
                wartosci.append(i[0])
        else:
            for _ in range(weight // i[1]):
                wagi.append(i[1])
                wartosci.append(i[0])
            
    dp = [0 for _ in range(weight + 1)]
    
    for i in range(len(wagi)):
        for j in range(weight, wagi[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - wagi[i]] + wartosci[i])
            
    return dp[weight]


print("Example:")
print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12

print("The mission is done! Click 'Check Solution' to earn rewards!")

