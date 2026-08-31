class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # load pref suf with 1s
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        res = []
        # prefix + suffix of i 

        # [1, 2, 3]
        # pref: [1, 1, 1]
        # go:
        # pref: [1, 1, 1]
        # pref: [1, 1, 1]
        # pref: [1, 1, 2]
        
        # fill prefixes:
        for i in range(len(nums) - 1):
            prefixes[i+1] = prefixes[i] * nums[i]

        for i in range(len(nums)-1, 0, -1):
            suffixes[i-1] = suffixes[i] * nums[i]    
        # print(prefixes)
        # print(suffixes)
        for i in range(len(prefixes)):
            res.append(prefixes[i] * suffixes[i])
        # print(res)
        return res





