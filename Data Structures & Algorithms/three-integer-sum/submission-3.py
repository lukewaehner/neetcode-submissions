class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while k > j:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while k > j and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return res