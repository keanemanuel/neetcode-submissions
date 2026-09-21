class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        highest = 1
        for n in nums:
            # find anchor
            if n-1 not in nums:
                consecutive = 1
                while n+consecutive in nums:
                    consecutive += 1
                    highest = max(consecutive, highest)
        return highest  