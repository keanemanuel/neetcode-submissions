class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))
        highest = consecutive = 1
        for i in range (1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                consecutive += 1
                highest = max(consecutive, highest)
            else:
                consecutive = 1
        return highest