class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left, best, seen = 0, 0, set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[i])
                best = max(best, i-left+1)
        return best