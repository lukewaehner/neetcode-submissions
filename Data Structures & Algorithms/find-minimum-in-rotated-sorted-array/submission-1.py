class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = l + (r-l) // 2
            # track any better minimum
            res = min(res, nums[m])
            # if the right point in our search is less than the middle, the rotation happened exclusively right
            # we shift into the right side
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                # the inverse stands for the left side
                r = m - 1
        # after the two pointers have met, we are guarantted to have homed in on the minimum point, since there is no (stop at the minimum here)
        return res
