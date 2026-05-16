class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        L = [-1]*n
        R = [n]*n
        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                # we want prev < so area = h * width
                stack.pop()
            L[idx] = stack[-1] if stack else -1
            stack.append(idx)
        stack.clear()
        for idx in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[idx]:
                stack.pop()
            R[idx] = stack[-1] if stack else n
            stack.append(idx)
        best = 0
        for i, h in enumerate(heights):
            best = max(best, h * (R[i] - L[i] - 1))
        return best
        


        