import math

class Solution:
    def testSpeed(self, t, ps, h):
        mt = 0
        for p in ps:
            mt += math.ceil(p / t)
        if mt <= h:
            return True
        else:
            return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles) # the absolute maximum needed - we can eat p piles at max_k because len(piles) >= h
        res = -1 # the target result
        l, r = 1, max_k
        while l <= r:
            m = (l + r) // 2
            print(m)
            print(self.testSpeed(m, piles, h))
            if self.testSpeed(m, piles, h):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


