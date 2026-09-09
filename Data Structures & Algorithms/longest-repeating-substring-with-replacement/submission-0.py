class Solution:
    def needShrinking(self, hm, k):
        m = max(hm.values()) if hm else 0
        tot = sum(hm.values())
        nuniq = tot - m
        return nuniq > k


    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return k
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        heat = {}
        ret = 0
        l = 0
        for r in range(len(s)):
            heat[s[r]] = heat.get(s[r], 0) + 1
            while self.needShrinking(heat, k):
                heat[s[l]] -= 1
                l += 1
            ret = max(ret, r - l + 1)
        return ret


