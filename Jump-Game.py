# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True

        if len(nums) == 1:
            return True

        for i in range(len(nums)):
            if dp[i]:
                for k in range(i + 1, i + nums[i] + 1):
                    if k == len(nums) - 1:
                        return True
                    else:
                        dp[k] = True
            else:
                return False