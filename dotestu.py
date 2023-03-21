import math
import heapq
from collections import Counter as C
from itertools import accumulate
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

def lastStoneWeight(stones):
        kol = []

        for i in stones:
            heapq.heappush(kol, -1 * i)

        while len(kol) > 1:
            k1 = -heapq.heappop(kol)
            k2 = -heapq.heappop(kol)
            
            if k1 != k2:
                heapq.heappush(kol, max(k1, k2) - min(k1, k2))
            else:
                continue
            
        if len(kol) == 0:
            return 0
        return abs(kol[0])

lastStoneWeight([2,2])
