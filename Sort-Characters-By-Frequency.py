# https://leetcode.com/problems/sort-characters-by-frequency/description/

import heapq
from dataclasses import dataclass

@dataclass
class literka:
    co : str
    ile : int

    def __lt__(self, other):
        return self.ile > other.ile
    
def main(s):
    zlicz = {}
    w = ""

    for i in s:
        if i not in zlicz:
            zlicz[i] = 0
        zlicz[i] += 1

    kol = []

    for i in zlicz:
        kol.append(literka(i, zlicz[i]))

    heapq.heapify(kol)

    while len(kol) > 0:
        i = heapq.heappop(kol)
        w += i.co * i.ile

    return w
    
print(main("abaccadeeefaafcc"))