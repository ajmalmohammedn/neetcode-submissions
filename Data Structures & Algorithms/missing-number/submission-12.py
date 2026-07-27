class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        for i in range(1, len(nums)+1):
            xor1 ^= i
        for num in nums:
            xor2 ^= num
        return xor1 ^ xor2