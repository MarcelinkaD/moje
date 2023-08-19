# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/4153/

from collections import Counter as C

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n - 1)
            w = ""
            akt_w = 1

            if len(s) == 1:
                return "11"

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    akt_w += 1
                else:
                    w += str(akt_w)
                    w += s[i - 1]
                    akt_w = 1

            w += str(akt_w)
            w += s[-1]
            akt_w = 1


            return w
        