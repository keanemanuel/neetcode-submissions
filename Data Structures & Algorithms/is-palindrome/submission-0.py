class Solution:
    def isPalindrome(self, s):
        newstring = "".join([c.lower() for c in s if c.isalnum()])
        return newstring == newstring[::-1]

        
        