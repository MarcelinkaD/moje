# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/

import math

class Solution:
    def mySqrt(self, n: int) -> int:
        pocz, kon = 0, n

        if n == 1:
            return 1

        while pocz <= kon:
            sr = (pocz + kon) / 2
            if sr * sr == n:
                return int(sr)
            elif kon - pocz < 1 and math.floor(pocz) == math.floor(kon):
                return math.floor(pocz)
            else:
                if sr * sr < n:
                    pocz = sr
                else:
                    kon = sr

        return int(pocz)
        