class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sm = {}
        l = 0
        ml = 0
        
        for r in range(len(s)):
            if s[r] in sm and sm[s[r]] >= l:
                l = sm[s[r]] + 1
                
            sm[s[r]] = r
            ml = max(ml, r - l + 1)
            
        return ml

