class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set: set(int) = set()

        for num in nums:
            if num in hash_set:
                return True
            else:
                hash_set.add(num)
        return False