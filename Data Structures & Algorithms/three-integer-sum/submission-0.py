class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i+1, n - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    answers.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return answers

        