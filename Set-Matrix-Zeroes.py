# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        gdzie = []
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for k in range(m):
                if matrix[i][k] == 0:
                    gdzie.append((i, k))

        for i in gdzie:
            matrix[i[0]] = [0 for i in range(m)]
            for j in range(n):
                matrix[j][i[1]] = 0