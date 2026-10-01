import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            hours = 0
            k = lo + (hi-lo) // 2
            for i in piles:
                hours += math.ceil(i/k)
            if hours <= h:
                hi = k
            elif hours > h:
                lo = k+1
        return lo