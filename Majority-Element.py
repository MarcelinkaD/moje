# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/824/

from collections import Counter as C

def majorityElement(l):
    c = C(l)
    w = 0
    
    for i in c:
        if c[i] > len(l) / 2:
            w = i

    return w