from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if strings don't have same length - impossible case
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        for c in s:
            counts[c] +=1
        for c in t:
            counts[c] -= 1
        
        return all(v == 0 for v in counts.values())
