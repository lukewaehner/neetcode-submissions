class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if target == nums[mi]:
                return mi
            elif target > nums[mi]:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1