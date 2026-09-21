class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()

        for key, value in enumerate(nums):
            if key > 0 and value == nums[key - 1]:
                continue

            left, right = key + 1, len(nums) - 1
            while left < right:
                total = value + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    solution.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1    
        return solution