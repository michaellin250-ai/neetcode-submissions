class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] 

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev_i = stack.pop() 
                result[prev_i] = i - prev_i 
            stack.append(i) 
        return result 