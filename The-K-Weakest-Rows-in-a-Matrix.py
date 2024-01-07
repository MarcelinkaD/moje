# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

from heapq import heapify, heappop, heappush
from dataclasses import dataclass

@dataclass
class row:
    suma : int
    kolejnosc : int
    
    def __lt__(self, other):
        if self.suma == other.suma:
            return self.kolejnosc < other.kolejnosc
        return self.suma < other.suma

def kWeakestRows(mat, k):
    kol = []
     
    for i in range(len(mat)):
        kol.append(row(sum(mat[i]), i))
        
    heapify(kol)
    w = []
    
    for _ in range(k):
        w.append(heappop(kol).kolejnosc)
        
    return w
    
print(kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))