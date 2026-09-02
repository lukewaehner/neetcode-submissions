class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r - l)
            # print(area)
            if area > max_water:
                max_water = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            # print(l,r)
            # print(heights[l], heights[r])
        return max_water