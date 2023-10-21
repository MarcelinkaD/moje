# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

from collections import Counter as C

def topKFrequent(l, k):
    w = set()
    c = dict(C(l))
    
    for _  in range(k):
        maxi = -1
        co = 0
        
        for i in c:
            if c[i] > maxi and i not in w:
                maxi = c[i]
                co = i
                
        w.add(co)
        
    return list(w)

print(topKFrequent([1,1,1,2,2,3], 2))
    