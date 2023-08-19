# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

class Solution:
    def czy_mozna(self, c):
        for i in c:
            if c[i] >= 2:
                return False
        return True

    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        
        c = {}
        ogon = 0
        glowa = -1
        akt_w = 0
        max_w = 0

        while ogon < len(s) - 1:
            while glowa < len(s) - 1 and self.czy_mozna(c):
                akt_w += 1
                glowa += 1

                if s[glowa] not in c:
                    c[s[glowa]] = 0

                c[s[glowa]] += 1

                if self.czy_mozna(c):
                    max_w = max(akt_w, max_w)

            akt_w -= 1
            c[s[ogon]] -= 1

            if self.czy_mozna(c):
                max_w = max(akt_w, max_w)

            ogon += 1

        return max_w