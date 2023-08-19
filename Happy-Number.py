# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/

class Solution:
    def isHappy(self, n: int) -> bool:
        pop_w = n
        sett = set([])

        while n != 1:
            nw = 0
            n = str(n)

            for i in range(len(n)):
                nw += int(n[i]) ** 2

            if nw in sett:
                return False
            else:
                n = nw
                sett.add(n)

        return True