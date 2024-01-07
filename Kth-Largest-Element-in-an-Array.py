# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq

def main(l, k):
    for i in range(len(l)):
        l[i] = -1 * l[i]
        
    heapq.heapify(l)
    
    while k > 1:
        k -= 1
        heapq.heappop(l)
        
    return -heapq.heappop(l)

print(main([3,2,1,5,6,4], 2))