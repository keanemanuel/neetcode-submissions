class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # contains [temp, index]
        
        for i, temp in enumerate(temperatures):
            # checks if stack non empty and gets the TEMPERATURE of the top stack
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([temp, i])
        return res