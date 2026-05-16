class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for idx, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                dist = idx - prev_index
                result[prev_index] = dist
            stack.append(idx)
        return result
        
        