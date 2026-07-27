class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for x in range(0, len(nums)+1):
            if x not in nums:
                return x
            else:
                continue