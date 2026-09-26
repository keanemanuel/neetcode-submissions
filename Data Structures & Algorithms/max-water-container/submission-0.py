class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best, curr = 0, 0
        left, right = 0, len(heights)-1
        while left < right:
            curr = min(heights[left], heights[right]) * (right-left)
            if curr > best:
                best = curr
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return best     