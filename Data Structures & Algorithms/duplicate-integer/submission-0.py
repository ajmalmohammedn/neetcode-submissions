class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_list = []
        for num in nums:
            if num in dup_list:
                return True
            else:
                dup_list.append(num)
        return False

