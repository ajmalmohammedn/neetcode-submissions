class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map: dict[int: int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in map:
                return [map[complement], i]
            else:
                map[num] = i