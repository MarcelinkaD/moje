# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w = {}
    
        for i in range(len(strs)):
            nowi = strs[i]
            nowi = ''.join(sorted(nowi))

            if nowi not in w:
                w[nowi] = [strs[i]]
            else:
                w[nowi].append(strs[i])

        nw = []

        for i in w:
            nw.append(w[i])

        return nw