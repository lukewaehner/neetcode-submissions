class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    # nums[l] is less less or the target and
                    # less than the midpoint, we have a sorted left
                    # segment, which target resides
                    r = m - 1
                else:
                    # The pivot hit somewhere within the left 
                    # side of the array
                    # we will not find target there
                    l = m + 1
            else:
                # the same logic applied on the right side
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1