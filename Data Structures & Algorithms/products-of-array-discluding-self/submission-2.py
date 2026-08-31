class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # load pref suf with 1s
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        res = []
        
        for i in range(len(nums) - 1):
            prefixes[i+1] = prefixes[i] * nums[i]
        for i in range(len(nums)-1, 0, -1):
            suffixes[i-1] = suffixes[i] * nums[i]    
        for i in range(len(prefixes)):
            res.append(prefixes[i] * suffixes[i])
        return res





