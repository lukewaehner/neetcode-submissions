class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while True:
            res = numbers[r] + numbers[l]

            if res == target:
                return [l + 1, r + 1]
            elif res > target:
                r -= 1
            else:
                l += 1
        return []