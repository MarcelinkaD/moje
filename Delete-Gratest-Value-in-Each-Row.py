# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

from heapq import heapify, heappop, heappush

def deleteGreatestValue(grid):
    kolejki = []
    w = 0
    
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            grid[i][k] = -1 * grid[i][k]
    
    for kolejka in grid:
        heapify(kolejka)
        kolejki.append(kolejka)
        
    while len(kolejki[0]) > 0:
        maxi = -1
        
        for kolejka in kolejki:
            maxi = max(maxi, -1 * heappop(kolejka))
            
        w += maxi
        
    return w
    
    
print(deleteGreatestValue([[10]]))