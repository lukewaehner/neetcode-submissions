class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search for an arbitrary minimum
        # but instead of the traditional target, scan the midpoint of left and right - this should give an alright sense of which direction needs to be gone in. 
        # if we hit a wall, do a segment shift to the other side of the array to make sure we haven't missed a chunk
        # we are tracking the minimum against with the condition l < r a rotation of the search window does not stand to hinder our performance
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = l + (r-l) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m - 1
        return res
