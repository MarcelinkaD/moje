# https://leetcode.com/problems/two-sum/

def twoSum(l, n):
    for i in range(len(l)):
        for k in range(i + 1, len(l)):
            if l[i] + l[k] == n:
                return [i, k]