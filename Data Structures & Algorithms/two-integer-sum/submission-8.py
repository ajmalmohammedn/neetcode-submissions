class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = dict()

        for i, num in enumerate(nums):
            if target - num in prev_map:
                return [prev_map[target - num], i]
            prev_map[num] = i
        return -1