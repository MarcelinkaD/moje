# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

class Solution:
    def czy_pal(self, c):
        if c == c[::-1]:
            return True
        else:
            return False
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s

        akt_w = 0
        max_w = 0
        str_w = ""

        for i in range(len(s)):
            for k in range(i, len(s)):
                if self.czy_pal(s[i : k + 1]):
                    if len(s[i : k + 1]) > max_w:
                        max_w = len(s[i : k + 1])
                        str_w = s[i : k + 1]

        return str_w
        