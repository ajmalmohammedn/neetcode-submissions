class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        sum_of_nums = (n*(n+1))//2
        
        for num in nums:
            res += num
        
        total = sum_of_nums - res
        return total