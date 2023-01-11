class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        t = target
        l = nums
        glowa = -1
        ogon = 0
        akt_wyn = 0
        lenl = 0
        w = 10000000000

        while ogon < len(l) - 1:
            while glowa < len(l) - 1 and akt_wyn < t:
                lenl += 1
                glowa += 1
                akt_wyn += l[glowa]

                if akt_wyn >= t:
                    w = min(lenl, w)
                    
                    
            akt_wyn -= l[ogon]
            ogon += 1
            lenl -= 1
            
            
            if akt_wyn >= t:
                w = min(lenl, w)

        if w == 10000000000:
            w = 0

        return w