import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = minRate = max(piles)

        while l<=r:
            rate = l + ((r-l)//2)

            rem = h
            for _, val in enumerate(piles):
                hoursUsed = math.ceil(val/rate)
                rem -= hoursUsed
                if(rem < 0): break
            
            if rem >= 0:
                if rate < minRate:
                    minRate = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return minRate

                
        