# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

def searchMatrix(l, n):
    for i in range(len(l)):
        for k in range(len(l[0])):
            if l[i][k] == n:
                return True
            
    return False