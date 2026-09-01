class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue
            if stack:
                current = stack[-1]
                if current == '(' and char == ')':
                    stack.pop()
                    continue
                if current == '{' and char == '}':
                    stack.pop()
                    continue
                if current == '[' and char == ']':
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False
        return stack == []