class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        cs = ""
        for c in s:
            if c.isalnum():
                cs += c.lower()
        print(cs)
        
        l = 0
        r = len(cs) - 1

        while l < r:
            if cs[l] != cs[r]:
               return False
            l += 1
            r -= 1
        return True
