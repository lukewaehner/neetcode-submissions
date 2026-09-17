from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1Count = Counter(s1)
        s2Count = Counter(s2[l:len(s1)])
        
        for r in range(len(s1), len(s2)):
            print(s1Count)
            print(s2Count)
            if s1Count == s2Count:
                return True
            s2Count[s2[l]] -= 1
            s2Count[s2[r]] += 1
            l += 1
        if s2Count == s1Count:
            return True

            
        return False
